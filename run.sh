#/bin/bash!

#   If "adress already in use" error, make
#   kill -9 $(ps -A | grep python | awk '{print $1}')

# Option:
# --param : parametrization mode - Full system administration
# --overview : overview mode - System overview

#Start program
mode=param
echo -e "[\033[1;34m#\033[0m] Run '\033[1;34mSystem Control Interface#\033[0m' in \033[1;32m$mode\033[0m mode"
sudo python3 main.py --$mode
