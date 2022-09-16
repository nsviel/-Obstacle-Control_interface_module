#---------------------------------------------
# Possible GET command:
# - /test_http_conn
# - /hu_state
# - /py_state
# - /image
#---------------------------------------------

from param import param_co
from HTTP import http_client_fct
from src import parser_json

import json


def get_state_hu():
    [ip, port, connected] = http_client_fct.network_info("hu")
    command = "/hu_state"
    data = http_client_fct.send_http_get(ip, port, connected, command)
    if(data != None):
        parser_json.update_state_file(param_co.path_state_hu, data)
        param_co.state_hu = json.loads(data)

def get_state_py():
    [ip, port, connected] = http_client_fct.network_info("py")
    command = "/py_state"
    data = http_client_fct.send_http_get(ip, port, connected, command)
    if(data != None):
        parser_json.update_state_file(param_co.path_state_py, data)
        param_co.state_py = json.loads(data)

def get_image(dest):
    [ip, port, connected] = http_client_fct.network_info(dest)
    command = "/image"
    data = http_client_fct.send_http_get(ip, port, connected, command)
    if(data != None):
        if(len(data) != 0):
            img = open(param_co.path_image, "wb")
            img.write(data)
            img.close()
