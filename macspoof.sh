#!usr/bin/bash
echo "Starting Mac Spoofer";
ifconfig wlan1 down;
macchanger -r wlan1;
ifconfig wlan1 up;
echo "Your mac is now spoofed, Hack Away!";
