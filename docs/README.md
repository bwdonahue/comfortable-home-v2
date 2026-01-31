# Comfortable Home v2

A modular, state-driven Home Assistant climate OS designed for comfort, stability, and seasonal automation.  
Includes Boost Mode, countdown logic, activity logs, and a structured approach to home rituals.

---

## 🌡️ Features

### **Boost Mode**
- Temporary comfort boost with automatic countdown  
- Cancel logic that resets UI and cooldowns  
- Dashboard tiles with live feedback  

### **Climate State Machine**
- Seasonal modes  
- Morning comfort routines  
- Raise/Lower quick adjustments with cooldown protection  
- Safety logic to prevent rapid cycling  

### **Activity Logging**
- Nest setpoint change detection  
- Climate activity feed  
- Clean, readable logs with timestamped entries  

### **Dashboard UX**
- Compact tiles  
- Color feedback  
- Quick actions  
- Live countdown display  

---

## 📘 Version History

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

---

## 📂 Repository Structure

config/
automations.yaml
scripts.yaml
scenes.yaml
templates/
customize.yaml  (optional)
docs/
architecture/
climate_os/
boost_logic/
changelog.md


---

## 🧠 Philosophy

Comfortable Home v2 is built around:

- Predictable behavior  
- Modular logic  
- Clean state transitions  
- Readable dashboards  
- Anxiety-proof automation design  
- A balance of stability and controlled novelty  

This system is designed to be teachable, maintainable, and expandable — a climate OS that grows with the home and the seasons.

---

## 🛠️ Requirements

- Home Assistant OS or Supervised  
- Nest integration  
- Input helpers (boolean, number, text)  
- Dashboard (Lovelace)  
- Basic YAML familiarity (optional — most logic is UI-based)

---

## 📄 License

