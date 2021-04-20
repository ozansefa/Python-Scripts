#!/usr/bin/env python

import requests


def getRequest(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

targetUrl = "google.com"

with open("/home/kali/Desktop/Scripts/subDomains.txt","r") as f:
    for line in f:
        word = line.strip()
        url =  targetUrl + "/" + word 
        response = getRequest(url)
        if response:
            print("[+] Discovered URL --> " + url)

