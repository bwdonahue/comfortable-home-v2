# Changelog

All notable changes to **Comfortable Home v2** are documented here.  
This project follows a simple, milestone-based versioning style.

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

