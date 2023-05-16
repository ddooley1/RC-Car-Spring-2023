#!/bin/bash
#This script runs on startup to enable functionality for the RC car
#If you want to disable this script, modify "etc/rc.local" and remove the line
#that runs this script.

# Connects "Mad Giga" BT Controller (change MAC address if using a different controller)
#MACADDRESS="00:90:E3:5B:12:FC"
# MAX_ATTEMPTS=20 
# CONNECTED=0

# date >> /home/pi/Desktop/debug.txt
#echo "startup.sh has started running..." >> /home/pi/Desktop/debug.txt

# Opens qjoypad for use w/ PS3 controller
lxterminal -e qjoypad "miniCar" &
#echo "qjoypad enabled..." >> /home/pi/Desktop/debug.txt

# Starts process needed for video streaming from camera
lxterminal -e sudo systemctl start motion

# Main Python script needed to run car
lxterminal -e python3 /home/pi/Desktop/RCcarSpring2023/RCcar.py
#echo "Python script running!" >> /home/pi/Desktop/debug.txt

#echo "startup.sh script has finished running" >> /home/pi/Desktop/debug.txt

