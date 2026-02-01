# **Comfortable Home v2**

A modular, state‑driven Home Assistant climate OS designed for comfort, stability, and seasonal automation.  
Includes Boost Mode, countdown logic, activity logs, seasonal email notifications, and a structured approach to home rituals.

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
- Seasonal modes (Spring, Fall, Shoulder Season)  
- Morning comfort routines  
- Raise/Lower quick adjustments with cooldown protection  
- Safety logic to prevent rapid cycling  
- Fully documented in `/docs/season_schedule.md` and `/docs/temperature_schedules.md`

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

### **v2.0 Beta — Jan 2026**  
IFTTT Automations + Dashboards

### **v2.1 Beta — Jan 2026**  
YAML Automations + UptimeRobot

### **v2.2 — Feb 2026**  
Logs + Temperature + Quick Buttons

### **v2.3 — Feb 2026**  
Boost Mode + Countdown System

### **v2.4 — Feb 2026**  
Stability + Cleanup + UI Migration

*(v2.5 will be added when officially released — ongoing changes live in `docs/CHANGELOG.md`)*

---

## **📂 Repository Structure**

```
COMFORTABLE-HOME/
│
├── .gitignore
├── .ha_run.lock
├── .HA_VERSION
├── automations.yaml
├── configuration.yaml
├── go2rtc-1.9.9
├── go2rtc.yaml
├── govee_learning.yaml
├── scenes.yaml
├── scripts.yaml
│
├── blueprints/
│
├── custom_components/
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
├── image/
│
├── templates/
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
```

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

