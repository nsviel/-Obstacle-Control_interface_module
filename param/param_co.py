#---------------------------------------------
import os, pwd


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

try:
    user = os.getlogin()
except:
    user = "."
path_ssd = "/media/" + user + "/lidar_ssd"

# Thread
run_loop = True;
run_thread_con = False
run_thread_image = False

# Socket
sock_server_l1 = None
sock_server_l2 = None

# Plot
nb_tic = 1000
last_x = 0
vec_x = []
vec_y_l1 = []
vec_y_l2 = []

# Wallet
wallet_add = ("localhost",)
wallet_ip = ("127.0.0.1",)

# Status
status_ui = "Development"
status_co = "Offline"
status_hu = "Offline"
status_py = "Offline"
status_ve = "Offline"
status_ai = "Offline"
status_ed = "Offline"
status_ssd = "Offline"
status_sncf = "Offline"
status_l1 = "Offline"
status_l2 = "Offline"
