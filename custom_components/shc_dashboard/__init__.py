"""Simple API backend for the SmartHome Copilot dashboard card."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.core import HomeAssistant
from homeassistant.components.http import HomeAssistantView
from homeassistant.components import persistent_notification
import homeassistant.helpers.config_validation as cv

import yaml
from pathlib import Path
import re

from ..smart_home_copilot.const import DOMAIN as COPILOT_DOMAIN


CONFIG_SCHEMA = cv.config_entry_only_config_schema

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: dict[str, Any]) -> bool:
    """Register API views used by the dashboard."""
    hass.http.register_view(CopilotSuggestionsView)
    hass.http.register_view(CopilotActionView)
    return True


class CopilotSuggestionsView(HomeAssistantView):
    """Expose generated suggestions via REST."""

    url = "/api/SmartHome_Copilot/suggestions"
    name = "SmartHomeCopilotSuggestions"
    requires_auth = True

    async def get(self, request):
        hass = request.app["hass"]
        suggestions = []
        counter = 0
        for coordinator in hass.data.get(COPILOT_DOMAIN, {}).values():
            data = getattr(coordinator, "data", {})
            for sug in data.get("suggestions", []):
                suggestions.append(
                    {
                        "id": counter,
                        "title": sug.get("title", "Automation Suggestion"),
                        "shortDescription": sug.get("description"),
                        "detailedDescription": sug.get("description"),
                        "yamlCode": sug.get("yaml"),
                        "provider": sug.get("provider", data.get("provider")),
                        "showDetails": False,
                    }
                )
                counter += 1
        return self.json(suggestions)


class CopilotActionView(HomeAssistantView):
    """Handle accept/decline actions for suggestions."""

    url = "/api/SmartHome_Copilot/{action}/{suggestion_id}"
    name = "SmartHomeCopilotAction"
    requires_auth = True

    async def post(self, request, action, suggestion_id):
        hass: HomeAssistant = request.app["hass"]
        coordinator = next(iter(hass.data.get(COPILOT_DOMAIN, {}).values()), None)
        if coordinator is None:
            return self.json({"success": False, "error": "No coordinator"})

        data = getattr(coordinator, "data", {})
        suggestions = data.get("suggestions", [])
        try:
            idx = int(suggestion_id)
            suggestion = suggestions[idx]
        except (ValueError, IndexError):
            return self.json({"success": False, "error": "Invalid suggestion id"})

        yaml_block = suggestion.get("yaml")
        if action == "accept" and yaml_block:
            placeholders = re.findall(r"<<([^>]+)>>", yaml_block)
            replaced = {}
            for ph in placeholders:
                tokens = re.split(r"[ _]+", ph.strip())
                domain = tokens[0].lower()
                keywords = [t.lower() for t in tokens[1:]]
                entities = hass.states.async_entity_ids(domain)
                if not entities:
                    continue
                replacement = None
                for ent in entities:
                    if all(k in ent.lower() for k in keywords):
                        replacement = ent
                        break
                if not replacement:
                    replacement = entities[0]
                yaml_block = yaml_block.replace(f"<<{ph}>>", replacement)
                replaced[ph] = replacement
            try:
                yaml.safe_load(yaml_block)
            except yaml.YAMLError as err:
                _LOGGER.error("Failed to parse YAML: %s", err)
                return self.json({"success": False, "error": "Invalid YAML"})

            if placeholders:
                msg_lines = [
                    "Placeholder mappings:",
                    *[f"{p} -> {replaced.get(p, 'unresolved')}" for p in placeholders],
                    "Please review the automation and adjust if needed.",
                ]
                persistent_notification.async_create(
                    hass,
                    "\n".join(msg_lines),
                    title="SmartHome Copilot Placeholder Mapping",
                    notification_id=f"ai_copilot_placeholder_{suggestion_id}",
                )

            file_path = Path(hass.config.path("automations.yaml"))
            file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(file_path, "a", encoding="utf-8") as f:
                if file_path.stat().st_size:
                    f.write("\n")
                f.write(yaml_block.rstrip() + "\n")

            await hass.services.async_call(
                "automation", "reload", blocking=True
            )
            _LOGGER.info("Suggestion %s accepted and automation reloaded", suggestion_id)
        elif action == "decline":
            _LOGGER.info("Suggestion %s declined", suggestion_id)

        # Remove handled suggestion
        suggestions.pop(idx)
        coordinator.data.update({"suggestions": suggestions})
        coordinator.async_set_updated_data(coordinator.data)
        await coordinator._async_save_suggestions()

        return self.json({"success": True})
