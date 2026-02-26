# **Comfortable Home v2**

A modular, state‑driven Home Assistant climate OS designed for comfort, stability, and seasonal automation.  
Includes Boost Mode, countdown logic, activity logs, seasonal email notifications, Shoulder Season intelligence, and expressive dashboard tiles.

---

## **📑 Table of Contents**
- [Features](#️-features)
- [Version History](#-version-history)
- [Repository Structure](#-repository-structure)
- [Philosophy](#-philosophy)
- [Requirements](#-requirements)
- [License](#-license)

---

## **🌡️ Features**

### **Boost Mode**
- Temporary comfort boost with automatic countdown  
- Cancel logic that resets UI and cooldowns  
- Dashboard tiles with live feedback  
- Clean, modular logic documented in `/docs/boost_mode.md`

### **Climate State Machine**
- Seasonal modes (Winter, Summer, Spring, Fall, Shoulder Season)  
- Morning comfort routines  
- Raise/Lower quick adjustments with cooldown protection  
- Safety logic to prevent rapid cycling  
- Fully documented in `/docs/season_schedule.md` and `/docs/temperature_schedules.md`

### **Shoulder Season Engine (v2.5)**
- Detects baseline days, warm‑day cooling, cool‑day heating, and Boost overrides  
- Color‑coded mode reporting  
- Nudge and baseline history with timestamped logs  
- Dashboard tiles styled to match Winter’s emotional readability  
- Unified NONE/unknown handling for clean idle states

### **Email Notifications**
- Seasonal mode email alerts  
- Embedded HTML templates  
- Test buttons on dashboard for previewing  
- Workflow documented in `/docs/updating_email_templates.md`

### **Activity Logging**
- Nest setpoint change detection  
- Climate activity feed  
- Clean, readable logs with timestamped entries  

### **Dashboard UX**
- Compact tiles  
- Color feedback  
- Quick actions  
- Live countdown display  
- Mushroom UI components stored in `/www/community/lovelace-mushroom/`

---

## **📘 Version History**

### **2.5.3 — Shoulder Season Engine + Dashboard Tiles (2026‑02‑25)**
First full implementation of the Spring/Fall Shoulder Season engine.  
Adds mode detection, nudge/baseline logs, and Winter‑style dashboard tiles.

### **2.5.2 — UptimeRobot Pause Hotfix (2026‑02‑15)**
Fixed REST payload regression after server migration.

### **2.5.1 — Seasonal Sunlight Engine + Dashboard Indicators (2026‑01‑31)**
Added sunlight detection, indicators, and dashboard tiles.

### **2.5.0 — Seasonal Email Templates + SendGrid Delivery (2026‑01‑??)**
Introduced HTML email templates and SendGrid delivery.

### **2.4 — Feb 2026**  
Stability + Cleanup + UI Migration

### **2.3 — Feb 2026**  
Boost Mode + Countdown System

### **2.2 — Feb 2026**  
Logs + Temperature + Quick Buttons

### **2.1 Beta — Jan 2026**  
YAML Automations + UptimeRobot

### **2.0 Beta — Jan 2026**  
IFTTT Automations + Dashboards

---

## **📂 Repository Structure**

COMFORTABLE-HOME/
│
├── automations.yaml
├── configuration.yaml
├── scenes.yaml
├── scripts.yaml
│
├── docs/
│   ├── boost_mode.md
│   ├── CHANGELOG.md
│   ├── email_templates_overview.md
│   ├── README.md
│   ├── season_schedule.md
│   ├── temperature_schedules.md
│   └── updating_email_templates.md
│
├── templates/
│   ├── shoulder_season_sensors.yaml
│   └── ...
│
└── www/
└── community/
└── lovelace-mushroom/
├── mushroom.js
├── mushroom.js.gz
└── email_templates/
├── shoulder.html
├── summer.html
└── winter.html

---

## **🧠 Philosophy**

Comfortable Home v2 is built around:

- Predictable behavior  
- Modular logic  
- Clean state transitions  
- Readable dashboards  
- Anxiety‑proof automation design  
- A balance of stability and controlled novelty  

This system is designed to be teachable, maintainable, and expandable — a climate OS that grows with the home and the seasons.

---

## **🛠️ Requirements**

- Home Assistant OS or Supervised  
- Nest integration  
- Input helpers (boolean, number, text)  
- Dashboard (Lovelace)  
- Basic YAML familiarity (optional — most logic is UI‑based)

---

## **📄 License**
MIT License
