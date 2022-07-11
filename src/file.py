#! /usr/bin/python
#---------------------------------------------

from param import param_co
from param import classes

from src import parser_json


def init_state():
    upload_config_file()
    update_state_file()

def upload_config_file():
    param_co.ip = parser_json.upload_state_lvl2_json(param_co.path_config, "self", "ip")
    param_co.port_sock_server = parser_json.upload_state_lvl2_json(param_co.path_config, "self", "sock_server_port")

    classes.hubium.ip = parser_json.upload_state_lvl2_json(param_co.path_config, "hubium", "ip")
    classes.hubium.sock_client_port = parser_json.upload_state_lvl2_json(param_co.path_config, "hubium", "sock_client_port")
    classes.hubium.http_server_port = parser_json.upload_state_lvl2_json(param_co.path_config, "hubium", "http_server_port")

def update_state_file():
    parser_json.update_state_lvl2_json(param_co.path_state_co, "self", "ip", param_co.ip)
    parser_json.update_state_lvl2_json(param_co.path_state_co, "self", "sock_server_port", param_co.sock_server_port)

    parser_json.update_state_lvl2_json(param_co.path_state_co, "hubium", "ip", classes.hubium.edge_ip)
    parser_json.update_state_lvl2_json(param_co.path_state_co, "hubium", "sock_client_port", classes.hubium.sock_client_port)
    parser_json.update_state_lvl2_json(param_co.path_state_co, "hubium", "http_server_port", classes.hubium.http_server_port)

def upload_hu_state():
    classes.hubium.status = parser_json.upload_state_lvl1_json(param_co.path_state_hu, "status")
    classes.hubium.ip = parser_json.upload_state_lvl1_json(param_co.path_state_hu, "ip")
