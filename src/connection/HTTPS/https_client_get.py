#---------------------------------------------
# Possible GET command:
# - /test_http_conn
# - /edge_state
# - /capture_state
# - /image
#---------------------------------------------

from src.param import param_control
from src.connection.HTTPS import https_client_fct
from src.utils import parser_json

import json


def get_state(dest):
    [ip, port, connected] = https_client_fct.network_info(dest)
    command = "/" + dest + "_state"
    data = https_client_fct.send_https_get(ip, port, connected, command)
    if(data != None):
        try:
            if(dest == "edge_1"):
                parser_json.update_state_file(param_control.path_state_edge_1, data)
                param_control.state_edge_1 = json.loads(data)
            elif(dest == "edge_2"):
                parser_json.update_state_file(param_control.path_state_edge_2, data)
                param_control.state_edge_2 = json.loads(data)
            elif(dest == "capture"):
                parser_json.update_state_file(param_control.path_state_capture, data)
                param_control.state_capture = json.loads(data)
            elif(dest == "network"):
                parser_json.update_state_file(param_control.path_state_perf, data)
                param_control.state_network = json.loads(data)
        except:
            print("get state marche pas")
            pass

def get_image(dest):
    [ip, port, connected] = https_client_fct.network_info(dest)
    command = "/image"
    data = https_client_fct.send_https_get(ip, port, connected, command)
    if(data != None):
        if(len(data) != 0):
            img = open(param_control.path_image, "wb")
            img.write(data)
            img.close()
            return True
    return False
