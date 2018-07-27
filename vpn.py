#!/bin/python
import subprocess
import time


loc = str(input("Enter a location "))
subprocess.call(["sudo", "systemctl", "enable", "expressvpn.service"])


def vpn(loc):
    import subprocess
    subprocess.call(["expressvpn", "disconnect"])
    time.sleep(.500)
    subprocess.call(["expressvpn", "disconnect"])
    subprocess.call(["expressvpn", "connect", loc])


time.sleep(.300)
subprocess.call(["sudo", "systemctl", "stop", "expressvpn.service"])
time.sleep(.300)
subprocess.call(["sudo", "systemctl", "restart", "expressvpn.service"])

if loc == "list":
    subprocess.call(["expressvpn", "disconnect"])
    time.sleep(.500)
    subprocess.call(["expressvpn", "disconnect"])
    subprocess.call(["expressvpn", "list"])
    loc1 = input("Enter a location")
    vpn(loc1)
else:
    vpn(loc)
