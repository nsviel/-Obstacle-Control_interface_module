#---------------------------------------------
from src.state import state_
import os, pwd


state = state_.State()


# State
state_control = {}
state_edge_1 = {}
state_edge_2 = {}
state_ground = {}
state_network = {}

# Path
path_state_control = "src/state/state_control.json"
path_state_capture = "src/state/state_capture.json"
path_state_edge_1 = "src/state/edge_1/state_edge.json"
path_state_edge_2 = "src/state/edge_2/state_edge.json"
path_state_perf = "src/state/edge_1/state_kpi.json"
path_image = "src/state/edge_1/image"
path_config = "config.json"
path_ssd = "/app/lidar_ssd"
path_node_coordinate = "src/gui/background/scheme_position.json"

# GUI
gui_fullscreen = False
gui_font_def = None
gui_font_big = None

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
