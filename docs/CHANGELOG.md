# Changelog

All notable changes to **Comfortable Home v2** are documented here.  
This project follows a simple, milestone-based versioning style.

---

## 2.7 — Vacation Mode System + Safety Bands + Return Prep (2026‑07‑24)

### Added
- Introduced full **Vacation Mode subsystem** with dedicated helpers:
  - `input_boolean.vacation_mode`
  - `input_boolean.hvac_paused`
  - `input_boolean.return_prep_mode`
  - `input_boolean.hard_weather_mode`
  - `input_boolean.boost_mode` (integrated into safety logic)
  - `input_text.vacation_mode_heartbeat`
  - `input_text.vacation_safety_high_log`
  - `input_text.vacation_safety_low_log`
  - `input_text.vacation_cold_snap_log`
  - `input_text.vacation_daily_safety_log`
  - `input_text.vacation_return_date`

- Added **11 dedicated Vacation Mode automations**, including:
  - **Vacation Mode Activation (Calendar‑Driven)** — activates Vacation Mode at the start of the trip.
  - **Vacation Mode Deactivation (Calendar‑Driven)** — disables Vacation Mode when the trip ends.
  - **Safety — Vacation Safety Band High** — prevents indoor temperature from exceeding 85°F.
  - **Safety — Vacation Safety Band Low** — prevents indoor temperature from dropping below 55°F.
  - **Safety — Cold Snap Protection** — protects the home during extreme cold.
  - **Safety — Heat Wave Protection** — protects the home during extreme heat.
  - **Safety — Humidity Protection** — prevents high indoor humidity using `sensor.thermostat_humidity`.
  - **Notification — Daily Safety Audit** — sends a 6 AM daily safety report.
  - **Stage 3 — Return Prep Mode** — activates HVAC prep the night before returning.
  - **Stage 4 — Return Prep Completion** — restores normal HVAC behavior after arrival.
  - **Vacation Heartbeat Writer** — writes a live status heartbeat every 15 minutes.

- Added **Slack webhook notifications** (`rest_command.slack_webhook_prod`) for:
  - Safety Band High triggers  
  - Safety Band Low triggers  
  - Cold Snap / Heat Wave events  
  - Daily Safety Audit  
  - Return Prep activation  
  - Vacation Mode ON/OFF transitions  

- Added **cooldown helpers** for all safety automations to prevent rapid re‑triggering:
  - Cold Snap  
  - Heat Wave  
  - Safety Band High  
  - Safety Band Low  
  - Humidity Protection  
  - Daily Safety Audit  

- Added **Hard Weather Mode** integration:
  - Auto‑activates based on Tempest + forecast  
  - Adjusts runtime expectations  
  - Adjusts anomaly thresholds  
  - Increases cooling aggressiveness  

- Added **HVAC Paused** subsystem:
  - Pauses all adaptive logic during Vacation Mode  
  - Prevents thermostat automation conflicts  
  - Ensures safe HVAC operation during extended absence  

### Improved
- Replaced invalid `state_not` conditions with safe template guards across all automations.
- Added first‑run protection for all cooldown templates using `last_changed is not none`.
- Standardized Slack JSON payloads for consistent logging and ingestion.
- Unified timestamp formatting across all Vacation Mode logs.
- Added guardrails to prevent:
  - thermostat off‑state misfires  
  - stale sensor triggers  
  - runaway safety loops  
  - premature Return Prep activation  
- Updated humidity logic to use `sensor.thermostat_humidity` instead of non‑existent entities.
- Cleaned up all numeric_state conditions for reliability and HA compatibility.

### Notes
This release introduces the **Comfortable Home V2 Vacation Brain** — a fully autonomous, safety‑aware, seasonally intelligent system designed for extended travel.  
It includes robust safety bands, cold/heat protection, daily audits, Slack notifications, Return Prep, and a full heartbeat system.  
All logic is hardened with cooldowns, guardrails, and sensor validation.  
This subsystem lays the foundation for Phase 2: **presence‑driven activation**, early‑return detection, accidental toggle protection, and calendar‑presence fusion.

---

## 2.6 — Maintenance Mode System + Slack/HA Notifications (2026‑07‑14)

### Added
- Introduced full Maintenance Mode subsystem for safe HVAC shutdowns during cleaning, repairs, or brownouts.
- Added new helpers:
  - `input_boolean.maintenance_mode`
  - `input_boolean.maintenance_mode_manual`
  - `input_text.previous_hvac_mode`
  - `input_text.maintenance_log`
- Added five dedicated automations:
  - **Enable Maintenance Mode When Nest Is Turned Off** — activates Maintenance Mode when Nest reports `off` or `unavailable`.
  - **Disable Maintenance Mode When Nest Is Turned On** — deactivates Maintenance Mode when Nest resumes heating/cooling.
  - **Maintenance Mode Enabled — Store Mode & Turn Off Nest** — captures previous HVAC mode and safely powers down the thermostat.
  - **Maintenance Mode Disabled — Restore Previous Mode** — restores the exact HVAC mode used before Maintenance Mode was activated.
  - **Manual Maintenance Mode Control** — allows manual toggling without touching the thermostat.
- Added Slack webhook notifications (`rest_command.slack_webhook_prod`) for:
  - Maintenance Mode enabled
  - Maintenance Mode disabled
  - Manual toggles
- Added Home Assistant persistent notifications for visibility inside the HA UI.

### Improved
- Added guardrails to prevent invalid HVAC mode restores, toggle loops, and brownout‑related misfires.
- Added timing delays to ensure Nest is ready before receiving restore commands.
- Standardized logging format in `input_text.maintenance_log` for consistent timestamping and readability.

### Notes
This release introduces a fully self‑contained Maintenance Mode engine designed for reliability, safety, and transparency.  
All actions are logged, all transitions are visible, and the system now includes multi‑channel notifications for complete operational awareness.  
This subsystem lays the groundwork for future enhancements such as dashboard banners, restart‑blocked warnings, and maintenance analytics.

---

## v1.0 — Notion Logging + Seasonal Architecture Overhaul (2026‑03‑04)

- Added unified seasonal activation automations (Spring, Summer, Fall, Winter)
- Added input_select.current_season for season-aware logic
- Added 19 Notion log automations across all seasons
- Converted all logs to event-driven state_changed triggers
- Removed all input_text rewrites to eliminate loops
- Standardized JSON payloads for Notion ingestion
- Added baseline, comfort, and weather-driven modes per season
- Prepared system for AI-generated summaries and daily climate reports

---

## 2.5.3 — Shoulder Season Engine + Dashboard Tiles (2026‑02‑25)

### Added
- Full Spring/Fall Shoulder Season engine with mode detection:
  - Baseline days
  - Warm-day cooling
  - Cool-day heating
  - Boost-aware behavior
- New template sensors:
  - `sensor.shoulder_season_current_log`
  - `sensor.shoulder_season_mode_color`
  - `sensor.shoulder_last_nudge_text`
  - `sensor.shoulder_last_nudge_color`
  - `sensor.shoulder_last_baseline_text`
- Three new dashboard tiles:
  - Shoulder Season Mode
  - Last Nudge
  - Last Baseline

### Improved
- Unified handling of `NONE` / `unknown` states for nudges and baselines.
- Grey “None” state before first events for cleaner idle UI.
- Matched Winter tile layout, emoji style, and timestamp formatting for visual consistency.

### Notes
This release is the first full implementation of the Shoulder Season engine
within Comfortable Home v2, extending Winter-style clarity into Spring and Fall.

---

## 2.5.2 — UptimeRobot Pause Hotfix (2026‑02‑15)

### Fixed
- Corrected UptimeRobot pause API payload after server migration.
- Updated REST command to use proper integer flag (`status: 0`) instead of string.
- Restored full pause/resume functionality for monitoring automation.

### Notes
This was a targeted **hotfix** applied outside the normal feature workflow to
address a post‑migration regression. No other systems were affected.

---

## 2.5.1 — Seasonal Sunlight Engine + Dashboard Indicators (2026‑01‑31)

### Added
- Sunny/Cloudy indicator system using dedicated input_booleans for Winter and Summer modes
- Mushroom dashboard cards for all four sunlight states with color‑coded icons and multiline logs
- 1‑hour auto‑clear behavior for sunlight indicators
- Visual feedback layer that mirrors real‑time sunlight logic without affecting seasonal mode

### Improved
- All four sunlight automations (Winter Sunny, Winter Cloudy, Summer Sunny, Summer Cloudy) now include:
  - 5‑minute catch‑up triggers for reliable recovery after clouds or cooldown
  - Boost‑aware conditions that fully pause sunlight logic during temporary overrides
  - Clean, predictable behavior across all sun/cloud transitions
- Dashboard readability and expressiveness through unified card layout and icon logic

### Fixed
- Eliminated edge cases where sunlight automations could fail to re‑trigger after cooldown or time windows
- Ensured indicator lights never conflict with seasonal mode status

---

## v2.5 — Feb 2026  
**Seasonal Email Templates + SendGrid Delivery**

### Added
- Introduced dedicated HTML email templates stored in `/config/www/email_templates/`
- Added seasonal templates: `winter.html`, `spring.html`, `summer.html`, `fall.html`
- Implemented SendGrid email delivery using `notify.sendgrid`
- Added “Last Seasonal Email Sent” timestamp sensors for visibility

### Updated
- Seasonal activation automations now trigger matching email‑sending automations
- Email‑sending automations now:
  - Load HTML templates via `!include www/email_templates/<season>.html`
  - Send formatted emails through SendGrid
  - Log send events
  - Update timestamp sensors

### Added — Preview System
- Added dashboard Preview Buttons for each seasonal email
- Preview buttons manually trigger the email‑sending automation without activating the season

### Improved Architecture
- Split seasonal logic into:
  1. **Season Activation Automation** — handles mode switching, thermostat adjustments, sensor updates, and triggers the email automation  
  2. **Email Sending Automation** — loads HTML, sends email, logs timestamp  
- Ensures clean separation of responsibilities and easier debugging

---

## v2.4 — Feb 2026  
**Stability + Cleanup + UI Migration**
- Migrated Boost Countdown from YAML to UI templates  
- Removed duplicate helpers and entities  
- Cleaned up automation visibility (Logbook/History)  
- Eliminated template warnings  
- Improved dashboard tiles and state feedback  
- Refined Boost Cancel logic to reset Raise/Lower cooldowns  

---

## v2.3 — Feb 2026  
**Boost Mode + Countdown System**
- Added Temporary Boost with automatic timer  
- Created Boost Countdown sensor  
- Added Boost Cancel logic  
- Implemented Raise/Lower cooldown protection  
- Added dashboard tiles with live countdown  
- Introduced state-aware climate adjustments  

---

## v2.2 — Feb 2026  
**Logs + Temperature + Quick Buttons**
- Added temperature logs and activity tracking  
- Introduced Raise/Lower quick buttons  
- Added Nest setpoint detection  
- Improved dashboard readability and UX  

---

## v2.1 Beta — Jan 2026  
**YAML Automations + UptimeRobot**
- Migrated from IFTTT to native YAML automations  
- Added UptimeRobot monitoring  
- Introduced early logging helpers  
- First structured climate routines  

---

## v2.0 Beta — Jan 2026  
**IFTTT Automations + Dashboards**
- Initial dashboards  
- IFTTT-based climate automations  
- First-generation comfort routines  
- Early visual feedback experiments  

---
