#! /usr/bin/python
#---------------------------------------------

from param import param_py

import json


# State
#--------------------
status = "Offline"
ip = "127.0.0.1"
#--------------------

# Hubium
sock_server_port = 1
sock_client_port = 1
http_server_port = 1

# MQTT
mqtt_connected = False
mqtt_topic = "ai_obstacle"
mqtt_ip = "127.0.0.1"
mqtt_port = 1

# Edge
edge_connected = False
edge_ip = "127.0.0.1"
edge_port = 1

# Valeo
vale_connected = False
valeo_ip = "127.0.0.1"
valeo_port = 1

# Velodium
velo_connected = False
velo_port = 1

# AI
ai_connected = False

# Path
path_capture = ""
path_dir_l1 = ""
path_dir_l2 = ""
path_file_l1 = ""
path_file_l2 = ""
path_name = ""
