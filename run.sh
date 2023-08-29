#/bin/bash!
# Author : Nathan Sanchiz-Viel

#   If "adress already in use" error, make
#   kill -9 $(ps -A | grep python | awk '{print $1}')

#Start program
mode=param
echo -e "[\033[1;34m#\033[0m] Run '\033[1;34mSystem Control Interface#\033[0m'"
sudo python3 main.py
