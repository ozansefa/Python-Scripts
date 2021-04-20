#!/bin/python

import sys
import socket

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  #Translate hostname to IPv4
else:
    print("Invalid amount of arguments")
    print("Syntax: python3 portScanner.py <ip>")

try:

    for port in range(1,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #IPv4 and Port
        socket.setdefaulttimeout(1) 

        resault = s.connect_ex((target, port)) 
        if resault == 0:
            print(f"Port {port} is open ")
        s.close()

except KeyboardInterrupt:
        print("\n Exitting Program !!!!")
        sys.exit()
except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
except socket.error:
        print("\ Server not responding !!!!")
        sys.exit()