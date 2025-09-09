⚠️ **Disclaimer**: Educational purpose only. Do not test on systems you don’t own or have explicit permission for.

---

# ⚡ Cross-Site Scripting (XSS, Reflected) – DVWA

## 🔍 Objective
Exploit **Reflected XSS** vulnerability to execute JavaScript code in the victim’s browser.

---

## 🛠️ Steps Taken

1. **Testing Input**
   - Chose *XSS (Reflected)* module in DVWA.
   - Entered payload:
     ```html
     <script>alert('XSS')</script>
     ```
   - Browser executed → Alert pop-up confirmed vulnerability.

2. **Refined Payload**
   - Used payload:
     ```html
     <img src=x onerror=alert("XSS_Demo_Triggered")>
     ```
   - Works without `<script>` tag → Bypasses basic filters.

3. **Automation with Python**
   - Created `xss_reflected.py`
   - Script:
     - Sends payload via `GET` parameter
     - Checks if payload is reflected in server response
     - Confirms injection

4. **Proof**
   - Browser pop-up alert triggered
   - Script detected reflected payload in HTML response

---

## 📸 Proof
- Screenshot: Alert pop-up (`XSS_Demo_Triggered`)
- Screenshot: Python script detecting reflected payload

---

## ✅ Result
Successfully exploited **Reflected XSS**:
- Injected payload executed in browser
- Vulnerability confirmed both **manually** and **via automation**


## ⚠️ Disclaimer

This project is created strictly for educational and research purposes only.
The tests shown here are performed on DVWA (Damn Vulnerable Web Application), a deliberately insecure environment designed for learning.
  - Do NOT use these techniques on any system, application, or    website that you do not own or do not have explicit permission to test.

  - Unauthorized hacking, exploitation, or intrusion into real systems is illegal and punishable under cybersecurity laws.

  - The author of this repository is not responsible for any misuse of the information or code provided.

By using this repository, you agree to use it only in safe, legal, and controlled environments like DVWA.