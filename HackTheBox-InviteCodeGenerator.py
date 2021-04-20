#!/usr/bin/env python3 

import requests
import base64

url = 'https://www.hackthebox.eu/api/invite/generate'
headers = {'content-type' : 'application/json', 'user-agent' : 'give me my INVITE CODE'}
x = requests.post(url, headers=headers)
data = x.json()
value = data['data']['code']
base = base64.b64decode(value)
print("Invite Code >> " + base.decode())