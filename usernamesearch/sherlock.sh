#! bin/bash
figlet Sherlock | lolcat
echo "Please Enter username you would like to search up: "
read name
cd ~
cd sherlock
python3 sherlock --nsfw $name
