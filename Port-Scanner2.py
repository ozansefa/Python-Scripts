#!/usr/bin/python3

import socket 

host = input("Please enter the IP you want to scan: ")
lowerOne = int(input("Please enter the lower value of the range : "))
higherOne = int(input("Please enter the higher value of the range : "))

def portScanner(host):
    for port in range(lowerOne,higherOne):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET => IPv4  SOCK_STREAM => TCP 
        sock.settimeout(0.05)
        if sock.connect_ex((host, port)) == 0: #calling connect_ex will raise an error
            print("Port {} is open".format(port))
        sock.close() 
portScanner(host)