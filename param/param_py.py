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
socket_connected = False
ssd_connected = False

# Parameter
path_config = "param/config.json"

# Thread
run_loop = True;
run_thread_con = False

# Socket
http_server_port = 1
sock_server_port = 1
sock_client = None

# Geolocalization
geo_country = "France"
