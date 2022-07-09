#! /usr/bin/python
#---------------------------------------------

from param import param_co
from param import param_hu
from param import param_py
from param import param_li

from src import parser_json


def init_state():
    upload_config_file()
    update_state_file()

def upload_config_file():
    param_co.ip = parser_json.upload_state_lvl2_json(param_co.path_config, "self", "ip")
    param_co.port_sock_server = parser_json.upload_state_lvl2_json(param_co.path_config, "self", "port_sock_server")

    param_co.edge_ip = parser_json.upload_state_lvl2_json(param_co.path_config, "edge", "ip")
    param_co.edge_port_sock_client = parser_json.upload_state_lvl2_json(param_co.path_config, "edge", "port_sock_client")
    param_co.edge_port_http_server = parser_json.upload_state_lvl2_json(param_co.path_config, "edge", "port_http_server")

def update_state_file():
    parser_json.update_state_lvl2_json(param_co.path_state_co, "self", "ip", param_co.ip)
    parser_json.update_state_lvl2_json(param_co.path_state_co, "self", "port_sock_server", param_co.port_sock_server)

    parser_json.update_state_lvl2_json(param_co.path_state_co, "edge", "ip", param_co.edge_ip)
    parser_json.update_state_lvl2_json(param_co.path_state_co, "edge", "port_sock_client", param_co.edge_port_sock_client)
    parser_json.update_state_lvl2_json(param_co.path_state_co, "edge", "port_http_server", param_co.edge_port_http_server)

def upload_hu_state():
    param_hu.status = parser_json.upload_state_lvl1_json(param_co.path_state_hu, "status")
    param_hu.ip = parser_json.upload_state_lvl1_json(param_co.path_state_hu, "status")
