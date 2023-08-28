#---------------------------------------------
import os, pwd


# State
state_control = {}
state_edge = {}
state_edge_2 = {}
state_ground = {}
state_network = {}
state_cloud = {}

# Path
path_state_current = "src/state/current/"
path_state_initial = "src/state/initial/"
path_node_coordinate = "src/state/scheme_position.json"
path_ssd = "/app/lidar_ssd"

# GUI
gui_fullscreen = False
gui_font_def = None
gui_font_big = None
gui_width = 1675
gui_height = 775

# Thread
run_loop = True;

# Tic delay
tic_loop = 0.033
tic_message = 0.05

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
status_control = "Offline"
status_edge_1 = "Offline"
status_capture = "Offline"
status_processing = "Offline"
status_ai = "Offline"
status_edge_2 = "Offline"
status_ssd = "Offline"
status_operator = "Offline"
status_lidar_1 = "Offline"
status_lidar_2 = "Offline"
status_db = "Offline"
