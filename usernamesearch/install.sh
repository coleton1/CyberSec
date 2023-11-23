#! bin/bash

cd ~
sleep 2
git clone https://github.com/sherlock-project/sherlock.git
sleep 2
cd sherlock
sleep 2
python3 -m pip install -r requirements.txt
echo "Sherlock successfuly installed!, Please use Sherlock.sh now." 
