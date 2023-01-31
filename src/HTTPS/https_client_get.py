#---------------------------------------------
# Possible GET command:
# - /test_http_conn
# - /hu_state
# - /py_state
# - /image
#---------------------------------------------

from src.param import param_co
from src.HTTPS import https_client_fct
from src.misc import parser_json

import json


def get_state(dest):
    [ip, port, connected] = https_client_fct.network_info(dest)
    command = "/" + dest + "_state"
    data = https_client_fct.send_https_get(ip, port, connected, command)
    if(data != None):
        try:
            if(dest == "hu"):
                parser_json.update_state_file(param_co.path_state_hu, data)
                param_co.state_hu = json.loads(data)
            elif(dest == "py"):
                parser_json.update_state_file(param_co.path_state_py, data)
                param_co.state_py = json.loads(data)
            elif(dest == "perf"):
                parser_json.update_state_file(param_co.path_state_perf, data)
                param_co.state_perf = json.loads(data)
        except:
            pass

def get_image(dest):
    [ip, port, connected] = https_client_fct.network_info(dest)
    command = "/image"
    data = https_client_fct.send_https_get(ip, port, connected, command)
    if(data != None):
        if(len(data) != 0):
            img = open(param_co.path_image, "wb")
            img.write(data)
            img.close()
            return True
    return False
