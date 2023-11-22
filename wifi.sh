#!/bin/bash
figlet WIFI SPAWNER | lolcat
#edit list of names in Documents 
airmon-ng start wlan0

echo "";
echo "Access points spawning....."
sleep 5
echo "Access points successfully created." | lolcat
echo "";
echo "";
echo "Press ctrl+c to Exit."
sudo mdk3 wlan0 b -c 1 -f /home/coletonb/Documents/wifi.lst





