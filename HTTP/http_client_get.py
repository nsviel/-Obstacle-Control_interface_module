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


def get_state(dest):
    [ip, port, connected] = http_client_fct.network_info(dest)
    command = "/" + dest + "_state"
    data = http_client_fct.send_http_get(ip, port, connected, command)
    if(data != None):
        parser_json.upload_file_by_sock_data(param_co.path_state_hu, data)
        param_co.state_hu = parser_json.load_file(param_co.path_state_hu)

def get_image(dest):
    [ip, port, connected] = http_client_fct.network_info(dest)
    command = "/image"
    data = http_client_fct.send_http_get(ip, port, connected, command)
    if(data != None):
        if(len(data) != 0):
            img = open(param_co.path_image, "wb")
            img.write(data)
            img.close()
