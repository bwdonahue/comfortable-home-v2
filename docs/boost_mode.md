# Temperature Boost Mode

Temperature Boost Mode is a temporary comfort override in Comfortable Home v2.  
It raises the heat or lowers the cooling setpoint for a short period, then automatically restores the system to its previous state without disrupting scheduled automations.

---

## 🎯 Purpose

Boost Mode exists to provide **short-term comfort** without breaking:

- seasonal schedules  
- solar-aware adjustments  
- Raise/Lower cooldown logic  
- the climate OS state machine  

It behaves like a real thermostat “temporary hold,” but with cleaner logic and better visibility.

---

## 🧩 Components

Boost Mode relies on the following helpers:

### **Input Booleans**
- `input_boolean.temporary_boost_active`  
  Indicates whether Boost Mode is currently running.

- `input_boolean.temporary_boost_direction_lock`  
  Prevents repeated Raise/Lower presses from stacking boosts.

### **Input Numbers**
- `input_number.temporary_comfort_original_temp`  
  Stores the thermostat temperature before the boost.

- `input_number.last_raise_press`  
  Used for cooldown logic to prevent rapid cycling.

### **Timer**
- `timer.temporary_comfort_timer`  
  Controls the duration of the boost (typically 1 hour).

---

## ⚙️ How Boost Mode Works

### **1. User presses Raise or Lower**
- System checks if a boost is already active  
- If not active, it:
  - Saves the current thermostat temperature  
  - Adjusts the setpoint by ±2°F  
  - Starts the 1-hour timer  
  - Activates the boost flag  
  - Locks direction to prevent stacking

### **2. Boost runs for the full duration**
- Dashboard shows a live countdown  
- Scheduled automations are paused  
- Solar logic is temporarily ignored  
- Raise/Lower cooldown is enforced

### **3. Boost ends automatically**
When the timer finishes:

- The original temperature is restored  
- Boost flag is turned off  
- Direction lock is cleared  
- Scheduled automations resume  
- Dashboard tiles reset

### **4. User can cancel early**
A “Cancel Boost” button:

- Stops the timer  
- Restores the original temperature  
- Clears all boost-related flags  
- Resets cooldown logic  

---

## 🛡️ Safety Logic

Boost Mode includes several protections:

- **Direction lock** prevents stacking boosts  
- **Cooldown** prevents rapid cycling  
- **Timer** ensures boosts never run indefinitely  
- **State restoration** ensures schedules resume cleanly  
- **Logging** tracks boost start/end events  

---

## 📊 Dashboard Integration

Boost Mode includes:

- A Boost tile with active/inactive states  
- A live countdown display  
- A Cancel Boost button  
- Color feedback when boost is active  

This gives the user immediate visibility into system state.

---

## 🧠 Design Philosophy

Boost Mode is built to be:

- **Predictable** — always returns to baseline  
- **Non-destructive** — never overwrites schedules  
- **Transparent** — visible countdown and logs  
- **Energy-aware** — integrates with solar logic  
- **Comfort-first** — quick, intuitive, reliable  

It behaves like a thermostat “temporary hold,” but with more intelligence and fewer surprises.

---

## 📦 Files Involved

- `automations.yaml`  
  - Boost Heat  
  - Boost Cool  
  - Boost Cancel  
  - Timer Finished → Reset

- `scripts.yaml`  
  - Optional helper scripts for reset logic

- `input_boolean.yaml` / UI helpers  
- `input_number.yaml` / UI helpers  
- `timer.yaml` / UI helpers  

---

## 🧭 Future Enhancements

- Adaptive boost duration based on season  
- Solar-aware boost scaling  
- Boost history log  
- Multi-room boost logic  
- Predictive comfort adjustments  

