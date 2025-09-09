# 🔐 DVWA Security Lab – Pentesting Automation

This project demonstrates **Web Application Penetration Testing** using [Damn Vulnerable Web Application (DVWA)](https://github.com/digininja/DVWA) in a safe, controlled environment (Kali Linux + PHP server).

⚠️ **Disclaimer**: Educational purpose only. Do not test on systems you don’t own or have explicit permission for.

---

## 📌 Features

- 💉 **SQL Injection (SQLi)**
  - Extracted user credentials with SQLMap
  - Cracked password hashes
  - Automated login with Python script (handles CSRF token + session cookies)

- ⚡ **Cross-Site Scripting (XSS, Reflected)**
  - Injected payload:  
    ```html
    <img src=x onerror=alert("XSS_Demo_Triggered")>
    ```
  - Automated detection with Python (`requests`, `BeautifulSoup`)
  - Verified reflected XSS by matching payload in server response

---

## 🛠️ Tech Stack
- **Python**: requests, BeautifulSoup4
- **Kali Linux + DVWA**
- **SQLMap** for SQL injection exploitation

---

## 📂 Project Structure
- `sql_injection/` → SQLi exploitation & login automation
- `xss_reflected/` → XSS reflected payload injection & automation
- `requirements.txt` → Python dependencies
- `README.md` → Documentation & instructions

---

## 🚀 How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. Run the SQLi login automation:
   ```bash
   python3 sql_injection/sqli_login.py

3. Run the XSS reflected automation:
   ```bash
   python3 xss_reflected/xss_reflected.py

---

## 📸 Screenshots (Proof of Work)
- SQL Injection
    - Users table dumped with SQLMap
    - Password hashes cracked
    - Auto-login script confirmed success

- XSS (Reflected)
    - Payload executed(Alert Box):
        ```html
        <img src=x onerror=alert("XSS_Demo_Triggered")>
    Verified in browser + via automation script

## 📖 Learning Outcomes
- Identified & exploited SQLi and XSS vulnerabilities
- Automated pentesting workflows with Python
- Handled sessions, cookies, CSRF tokens programmatically
- Documented end-to-end penetration testing methodology

---

## 🙌 Author

Developed by Siddharth Chaudhary.

---

## ⚠️ Disclaimer

This project is created strictly for educational and research purposes only.
The tests shown here are performed on DVWA (Damn Vulnerable Web Application), a deliberately insecure environment designed for learning.
  - Do NOT use these techniques on any system, application, or    website that you do not own or do not have explicit permission to test.

  - Unauthorized hacking, exploitation, or intrusion into real systems is illegal and punishable under cybersecurity laws.

  - The author of this repository is not responsible for any misuse of the information or code provided.

By using this repository, you agree to use it only in safe, legal, and controlled environments like DVWA.