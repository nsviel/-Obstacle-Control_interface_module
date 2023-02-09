#---------------------------------------------
import os, pwd


# State
state_co = {}
state_hu = {}
state_py = {}
state_perf = {}

# Path
path_state_co = "src/state/state_co.json"
path_state_hu = "src/state/state_hu.json"
path_state_py = "src/state/state_py.json"
path_state_perf = "src/state/state_perf.json"
path_image = "src/state/image"
path_image_empty = "src/state/image_empty"
path_config = "config.json"
path_ssd = "/app/lidar_ssd"

# GUI
gui_fullscreen = False
gui_font_def = None
gui_font_big = None

# Thread
run_loop = True;
run_thread_con = False
run_thread_image = False

# Tic delay
tic_loop = 0.033
tic_message = 0.05
tic_image = 0.1
tic_connection = 0.5

# Socket
sock_server_l1 = None
sock_server_l2 = None
lidar_main = "lidar_1"

# Plot
nb_tic = 1000
last_x = 0
vec_x = []
vec_y_l1 = []
vec_y_l2 = []

# Wallet - init with just locahost
wallet_add = ("localhost",)
wallet_ip = ("127.0.0.1",)

#Image
image_h = 0
image_w = 0

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
status_db = "Offline"

# Icon
path_icon_computer = "src/param/icon/computer.png"
path_icon_lidar = "src/param/icon/lidar.png"
path_icon_server = "src/param/icon/server.png"
path_icon_train = "src/param/icon/train.png"
path_icon_wifi = "src/param/icon/wifi.png"
path_icon_cloud = "src/param/icon/cloud.png"
path_icon_soft = "src/param/icon/compute.png"
path_icon_ssd = "src/param/icon/ssd.png"
path_icon_database = "src/param/icon/database.png"
