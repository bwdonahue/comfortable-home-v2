# Comfortable Home v2 — Seasonal Schedule

This document defines the official seasonal boundaries used by Comfortable Home v2.  
These dates determine when seasonal automations activate, when email reminders are sent, and how climate logic behaves throughout the year.

---

## 🌱 Spring Shoulder Season
**March 15 → May 14**

Spring Shoulder Season is the transitional period between winter heating and summer cooling.  
During this time, the system:

- Uses flexible temperature bands
- Minimizes rapid mode switching
- Sends the Spring Activation Email with reminders for:
  - Furnace filter check
  - Humidifier shutdown
  - Early AC inspection

---

## ☀️ Summer Mode
**May 15 → September 14**

Summer Mode is the primary cooling season.  
During this time, the system:

- Enables full cooling logic
- Disables humidifier logic
- Sends the Summer Activation Email with reminders for:
  - AC filter check
  - Condenser cleaning
  - Dehumidifier readiness

---

## 🍂 Fall Shoulder Season
**September 15 → November 14**

Fall Shoulder Season is the transition from cooling to heating.  
During this time, the system:

- Uses flexible temperature bands
- Avoids premature furnace activation
- Sends the Fall Activation Email with reminders for:
  - Furnace filter replacement
  - Humidifier pad installation
  - Thermostat battery check

---

## ❄️ Winter Mode
**November 15 → March 14**

Winter Mode is the primary heating season.  
During this time, the system:

- Enables full heating logic
- Activates humidifier logic
- Sends the Winter Activation Email with reminders for:
  - Humidifier setup
  - Furnace inspection
  - Winterization tasks

---

## Notes
- These dates are optimized for Chicagoland climate patterns.
- Seasonal activations are triggered automatically at midnight on the boundary date.
- Manual overrides are available via the Seasonal Dashboard.
