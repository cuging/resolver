#!/usr/bin/env python3.8
import sys, socket, os
try:
    x = input("Domain/IP: " )
    cping = os.system("ping -c3 " + x)
    if cping == 0:
        print(x.upper() + ' is UP!')
    else:
        print('ping to ' + x.upper() + ' is failed!')
    ns = os.system("host -t ns " + x)
    host = os.system("host " + x)
    ip = socket.gethostbyname(x)
    hostname = socket.gethostbyaddr(x)
    print("IP: ", ip)
    print("HOSTNAME: ", hostname[0])
except Exception:
    print('Hostname Unknown')
os.execl(sys.executable, sys.executable, * sys.argv)
