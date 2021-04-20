#!/usr/bin/env python

import subprocess

interface = input("Interface > ")
newMac = input("new MAC > ")

print("[+] Changing MAC adress for " + interface + "to " + newMac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", newMac])
subprocess.call(["ifconfig", interface, "up"])