#! /usr/bin/python
#---------------------------------------------

import os


# State
state_co = {}
state_hu = {}
state_py = {}

# Path
path_state_co = "state/state_co.json"
path_state_hu = "state/state_hu.json"
path_state_py = "state/state_py.json"
path_image = "state/image"
path_config = "param/config.json"
path_ssd = "/media/" + os.getlogin() + "/lidar_ssd"

# Thread
run_loop = True;
run_thread_con = False
run_thread_image = False

# Wallet
wallet_add = ("localhost",)
wallet_ip = ("127.0.0.1",)
