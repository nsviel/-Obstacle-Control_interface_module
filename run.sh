#/bin/bash!

#   If adress already in use
#   kill -9 $(ps -A | grep python | awk '{print $1}')

# Option:
# --dev : development mode
# --demo : demo mode

#Start program
sudo python3 main.py --dev
