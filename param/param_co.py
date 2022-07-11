#! /usr/bin/python
#---------------------------------------------
#Data and parameters for network connections
#---------------------------------------------

import os


# State
#--------------------
status = "Offline"
ip = "127.0.0.1"
#--------------------

# Connection
http_connected = False
sock_server_port = 1

# Parameter
gui_width = 1200
gui_height = 800

# Path
path_state_co = "state/state_co.json"
path_state_hu = "state/state_hu.json"
path_state_py = "state/state_py.json"
path_config = "param/config.json"

# Thread
run_loop = True;
run_thread_con = False

# SSD
ssd_connected = False
ssd_activated = True
ssd_path = "/media/" + os.getlogin() + "/lidar_ssd"
ssd_space_total = 0
ssd_space_used = 0

# Wallet
wallet_add = ("localhost",)
wallet_ip = ("127.0.0.1",)
