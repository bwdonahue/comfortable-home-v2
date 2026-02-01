# **Updating Email Templates (Comfortable Home v2)**

This guide explains how to update the embedded HTML email templates used by the **Seasonal Mode Email Automation**, regardless of whether you are editing from desktop VS Code, the Home Assistant VS Code add‑on, or any other text editor.

The workflow is always the same:

- **Edit the HTML inside the automation YAML**  
- **Commit/push (if using Git)**  
- **Pull into Home Assistant**  
- **Reload + test using dashboard buttons**

---

## **1. Automation Name & Location**

All email templates are embedded directly inside this automation:

### **Automation:**  
`automation.seasonal_mode_email_notification`

### **File Location:**  
```
/config/automations.yaml
```

(or wherever your automations are stored if split into multiple files)

This automation contains **three HTML templates**, one for each seasonal mode:

- **Spring Mode Email Template**  
- **Fall Mode Email Template**  
- **Shoulder Season Email Template**

Each template appears inside the automation under a `body: >` block.

---

## **2. Editing the HTML (Most Important Step)**

The HTML for each email is stored **inside the automation YAML**, not in external files.

To update a template:

1. Open your automations file in **any editor**  
   - Desktop VS Code  
   - HA VS Code add‑on  
   - Studio Code Server  
   - File Editor  

2. Locate the correct `body: >` block for the seasonal email you want to update  
3. Edit the HTML directly inside the YAML  
4. Use **single quotes `'`** inside HTML to avoid YAML parsing issues  
5. Keep indentation exactly the same  
6. Save the file  

### **Example structure:**

```yaml
body: >
  <html>
    <body style='font-family: Arial;'>
      <h1>Welcome to Shoulder Season</h1>
      <p>Your home has transitioned to a new mode.</p>
    </body>
  </html>
```

This is the only place the HTML lives.

---

## **3. Updating the Automation Logic (If Needed)**

If you need to adjust:

- subject lines  
- variables  
- service data  
- conditions  

…edit those sections in the same automation.

### **Example:**

```yaml
data:
  title: "Shoulder Season Update"
  data:
    html: "{{ email_html }}"
```

Keep indentation consistent.

---

## **4. Deploying Changes (If Using Git)**

If you are using Git (recommended):

### **Commit + Push**
From your editor’s Git panel or terminal:

```
git add .
git commit -m "Update Shoulder Season email template"
git push
```

### **Pull Into Home Assistant**
Inside HA’s VS Code add‑on terminal:

```
git pull
```

---

## **5. Reload Automations**

In Home Assistant:

**Settings → Developer Tools → YAML → Reload Automations**

This loads your updated HTML.

---

## **6. Test Using Dashboard Preview Buttons**

Your dashboard includes preview/test buttons for:

- Spring Mode Email  
- Fall Mode Email  
- Shoulder Season Email  

Tap the button for the template you updated and confirm the email renders correctly.

---

## **Summary**

- All three email templates live **inside one automation**  
- You edit the HTML directly in the YAML  
- Any editor works (desktop VS Code, HA VS Code, etc.)  
- Git workflow is optional but recommended  
- Dashboard buttons are your preview/testing tool  
