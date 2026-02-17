# Hotfix Log

This document records urgent, production‑level fixes applied outside the normal
feature workflow. Hotfixes are small, targeted patches made to restore expected
behavior after migrations, outages, or unexpected system changes.

---

## 2026‑02‑15 — UptimeRobot Pause Payload Fix

### Summary
After the Comfortable Home v2 server migration, the UptimeRobot integration
stopped correctly pausing monitors due to a malformed API payload. The system
was attempting to send a string value instead of the required integer flag.

### Root Cause
- Migration changed the environment where the API call was executed.
- The UptimeRobot API requires `"status": 0` (integer) for pause.
- The automation was sending `"status": "0"` (string), which the API silently ignored.

### Fix
- Updated the REST command payload to use the correct integer type.
- Validated the API response and confirmed proper pause behavior.
- Tested resume behavior to ensure no regressions.

### Impact
- Restored full UptimeRobot pause/resume functionality.
- No other systems were affected.
- No downtime beyond the initial discovery window.

### Classification
**Hotfix** — urgent, isolated, post‑migration patch.
