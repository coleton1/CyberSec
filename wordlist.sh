sl | lolcat
clear
echo"";
figlet -f "slant" Wordlist Maker | lolcat;
echo "";
echo "================================================================================" | lolcat
echo "You will now be redirected to vim, press i, insert your words to be wordlisted - seperated by a new line -" 
echo "When you have completed press esc, followed by :wq! and <enter>" 
echo "Your wordlist will be saved to the desktop as new.txt" 
echo "================================================================================" | lolcat
echo "";
sleep 5;
sudo touch Cpass.txt ;
sudo nano Cpass.txt;
sleep 7;
echo "(optional) Enter an option: "
read op
sudo rsmangler $op --file Cpass.txt --output new.txt;

