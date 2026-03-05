# Changelog

All notable changes to **Comfortable Home v2** are documented here.  
This project follows a simple, milestone-based versioning style.

## v1.0 — Notion Logging + Seasonal Architecture Overhaul (2026-03-04)

- Added unified seasonal activation automations (Spring, Summer, Fall, Winter)
- Added input_select.current_season for season-aware logic
- Added 19 Notion log automations across all seasons
- Converted all logs to event-driven state_changed triggers
- Removed all input_text rewrites to eliminate loops
- Standardized JSON payloads for Notion ingestion
- Added baseline, comfort, and weather-driven modes per season
- Prepared system for AI-generated summaries and daily climate reports

## 2.5.3 — Shoulder Season Engine + Dashboard Tiles (2026-02-25)

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

## 2.5.2 — UptimeRobot Pause Hotfix (2026‑02‑15)

### Fixed
- Corrected UptimeRobot pause API payload after server migration.
- Updated REST command to use proper integer flag (`status: 0`) instead of string.
- Restored full pause/resume functionality for monitoring automation.

### Notes
This was a targeted **hotfix** applied outside the normal feature workflow to
address a post‑migration regression. No other systems were affected.

## 2.5.1 — Seasonal Sunlight Engine + Dashboard Indicators (2026-01-31)

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

## **v2.5 — Feb 2026**  
**Seasonal Email Templates + SendGrid Delivery**

**Added**
- Introduced dedicated HTML email templates stored in `/config/www/email_templates/`
- Added seasonal templates: `winter.html`, `spring.html`, `summer.html`, `fall.html`
- Implemented SendGrid email delivery using `notify.sendgrid`
- Added “Last Seasonal Email Sent” timestamp sensors for visibility

**Updated**
- Seasonal activation automations now trigger matching email‑sending automations
- Email‑sending automations now:
  - Load HTML templates via `!include www/email_templates/<season>.html`
  - Send formatted emails through SendGrid
  - Log send events
  - Update timestamp sensors

**Added — Preview System**
- Added dashboard Preview Buttons for each seasonal email
- Preview buttons manually trigger the email‑sending automation without activating the season

**Improved Architecture**
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

