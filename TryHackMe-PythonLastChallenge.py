#!/usr/bin/env python3

import base64

with open("encodedflag.txt","r") as f:
    context = f.read()
    
code = ""

for i in range(0,5):
    code = base64.b16decode(context)
    flag = code

for i in range(0,5):
    code = base64.b32decode(context)
    flag = code

for i in range(0,5):
    code = base64.b64decode(context)
    flag = code

print(flag)