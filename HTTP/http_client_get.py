#! /usr/bin/python
#---------------------------------------------

from param import param_co
from HTTP import http_client_fct
from src import parser_json


def get_falsealarm():
    http_client_fct.send_command_request("/falsealarm", "[#] False alarm sended")

def get_lidar_1_start():
    http_client_fct.send_command_request("/lidar_1_start", "[#] Lidar 1 start")

def get_lidar_1_stop():
    http_client_fct.send_command_request("/lidar_1_stop", "[#] Lidar 1 stop")

def get_image():
    http_client_fct.send_image_request(param_co.path_image)

def get_state_hu():
    state = http_client_fct.send_state_request("/state_hu")
    if(state != None):
        parser_json.upload_file_by_sock_data(param_co.path_state_hu, state)
        param_co.state_hu = parser_json.load_file(param_co.path_state_hu)

def get_state_py():
    state = http_client_fct.send_state_request("/state_py")
    if(state != None):
        parser_json.upload_file_by_sock_data(param_co.path_state_py, state)
        param_co.state_py = parser_json.load_file(param_co.path_state_py)
