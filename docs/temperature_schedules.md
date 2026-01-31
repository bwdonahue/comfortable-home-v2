# Temperature Schedule System

The Temperature Schedule System forms the foundation of Comfortable Home v2. It defines how the home behaves across seasons, times of day, and weather conditions. Each schedule represents a predictable comfort block that activates only when its season is active and Boost Mode is not running.

---

## Seasonal Overview

The system is divided into four seasonal modes, each with its own set of schedules and nudges.

### Winter
- Winter Mode Activation  
- Winter Morning Comfort (6–10 AM)  
- Winter Weekday Daytime (10 AM–5 PM)  
- Winter Weekend Daytime (10 AM–5 PM)  
- Winter Sunny Heating  
- Winter Cloudy Heating  
- Winter Evening (5–11 PM)  
- Winter Overnight (11 PM–6 AM)  

### Summer
- Summer Mode Activation  
- Summer Morning Comfort (6–10 AM)  
- Summer Baseline (10 AM–8 PM)  
- Summer Sunny Cooling  
- Summer Cloudy Cooling  
- Summer Evening (8–11 PM)  
- Summer Overnight (11 PM–6 AM)  

### Spring (Shoulder Season)
- Spring Shoulder Season Activation  
- Spring Temperature Baseline (10 AM–8 PM)  
- Spring Cooling Nudge (Warm Shoulder Days)  
- Spring Heating Nudge (Cool Shoulder Days)  

### Fall (Shoulder Season)
- Fall Shoulder Season Activation  
- Fall Temperature Baseline (10 AM–8 PM)  
- Fall Cooling Nudge (Warm Shoulder Days)  
- Fall Heating Nudge (Cool Shoulder Days)  

---

## Core Logic Structure

Each schedule follows a consistent pattern:

### Time Trigger
Schedules activate at specific times (e.g., 6:00 AM, 10:00 AM, 5:00 PM).

### Seasonal Condition
Only runs if the correct season mode is active.

### Boost Mode Check
If Boost Mode is active, the schedule is skipped to avoid overriding temporary comfort.

### Temperature Adjustment
The system sets the thermostat to the appropriate target temperature for that block.

### Logging
Each schedule writes a timestamped entry to its log helper for dashboard visibility.

---

## Weather-Aware Adjustments

### Sunny Heating (Winter)
Uses solar gain to reduce furnace load.

### Cloudy Heating (Winter)
Maintains comfort when solar gain is low.

### Sunny Cooling (Summer)
Uses solar power to cool more aggressively during peak production.

### Cloudy Cooling (Summer)
Reduces cooling demand when solar output is low.

### Shoulder Season Nudges
Small adjustments based on outdoor temperature swings.

---

## Dashboard Integration

- Each schedule has a toggle for visibility and manual control  
- Tiles show last run time and target temperature  
- Color-coded states indicate active, skipped, or idle  
- Logs provide a readable history of schedule activity  

---

## Design Philosophy

The schedule system is designed to be:

- Predictable and easy to understand  
- Modular, with each block isolated for clarity  
- Seasonal, adapting to the rhythms of the year  
- Solar-aware, maximizing free energy when available  
- Resilient, with Boost Mode and safety checks  

---

## Future Enhancements

- Forecast-based schedule adjustments  
- Adaptive comfort curves  
- Battery-aware scheduling  
- Automated seasonal switching  
- Visual timeline editor for schedules
