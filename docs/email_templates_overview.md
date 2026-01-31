# Comfortable Home v2 — Email Templates Overview

This document explains how seasonal email templates work, how they are triggered, and how they integrate with the Seasonal Activation Automations.

---

## 📨 Purpose of Seasonal Emails

Each season has a dedicated HTML email template that provides:

- A clear seasonal welcome message
- A checklist of tasks to complete
- Links to service providers or documentation
- A summary of what the automation system is doing behind the scenes

These emails act as ritualized seasonal transitions — both practical and emotional — anchoring the shift between modes.

---

## 📁 Template Location

All templates live in:

/config/www/email_templates/


Current templates:

- `shoulder.html` (Spring/Fall shared structure)
- `summer.html`
- `winter.html`

---

## ⚙️ How Templates Are Used

Each template is sent using the `notify.sendgrid` service with HTML enabled.

Example service call:

```yaml
service: notify.sendgrid
data:
  title: "Winter Mode Activated"
  message: !include www/email_templates/winter.html

🔄 How Templates Are Triggered
Each season has two automations:

1. Season Activation Automation
This automation:

Sets the seasonal mode

Adjusts thermostats

Updates sensors

Calls the email‑sending automation

Example:

yaml
action:
  - service: automation.trigger
    target:
      entity_id: automation.send_winter_email
2. Email Sending Automation
This automation:

Loads the correct HTML template

Sends the email via SendGrid

Logs the timestamp

Updates the “Last Seasonal Email Sent” sensor

Example:

yaml
trigger:
  - platform: event
    event_type: send_winter_email
action:
  - service: notify.sendgrid
    data:
      title: "Winter Mode Activated"
      message: !include www/email_templates/winter.html
🧪 Preview Buttons
Each email automation includes a Preview Button on the Seasonal Dashboard.
This allows you to test the email without activating the season.

Preview buttons call the same email automation manually.

🧭 Summary
Seasonal email templates are:

HTML files stored in /config/www/email_templates

Sent by dedicated email automations

Triggered by seasonal activation automations

Previewable from the dashboard

Logged via timestamp sensors

They form the communication layer of Comfortable Home v2, ensuring every seasonal transition is clear, intentional, and actionable.