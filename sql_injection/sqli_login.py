#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DVWA Automated Login Script
---------------------------
For educational purposes only. 

This script demonstrates how to:
- Maintain sessions and cookies using `requests`
- Extract CSRF tokens with `BeautifulSoup`
- Automate a login workflow into DVWA

Do NOT use this script against systems you do not own or have explicit permission to test.
"""

import requests
from bs4 import BeautifulSoup

# ------------------------------
# DVWA URLs (replace <YOUR_LOCAL_IP> with your local DVWA instance IP/host)
# ------------------------------
login_url = "http://<YOUR_LOCAL_IP>/DVWA/login.php"
index_url = "http://<YOUR_LOCAL_IP>/DVWA/index.php"

# Start session (keeps cookies automatically)
session = requests.Session()

# STEP 1: Fetch login page (to get user_token + cookies)
login_page = session.get(login_url)
soup = BeautifulSoup(login_page.text, "html.parser")
user_token = soup.find("input", {"name": "user_token"})["value"]
print("[*] Extracted token:", user_token)

# STEP 2: Prepare login data
credentials = {
    "username": "<USERNAME>",     # Default DVWA username: admin
    "password": "<PASSWORD>",     # Default DVWA password: password
    "Login": "Login",
    "user_token": user_token
}

# Add headers to mimic browser
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)",
    "Content-Type": "application/x-www-form-urlencoded"
}

# STEP 3: Send POST request with login data
response = session.post(login_url, data=credentials, headers=headers)

# STEP 4: Test access by loading index.php (dashboard)
dashboard = session.get(index_url)

if "Welcome to Damn Vulnerable Web Application!" in dashboard.text:
    print(f"[+] Login successful with: {credentials['username']} / {credentials['password']}")
else:
    print("[-] Login failed or session cookie missing.")
    print(dashboard.text[:500])  # Debugging: print first 500 chars of response
