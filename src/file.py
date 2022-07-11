#! /usr/bin/python
#---------------------------------------------

from param import cla

from src import parser_json


def init_state():
    upload_config_file()
    update_state_file()

def upload_config_file():
    cla.contro.ip = parser_json.upload_state_lvl2_json(cla.contro.path_config, "self", "ip")
    cla.contro.port_sock_server = parser_json.upload_state_lvl2_json(cla.contro.path_config, "self", "sock_server_port")

    cla.hubium.ip = parser_json.upload_state_lvl2_json(cla.contro.path_config, "hubium", "ip")
    cla.hubium.sock_client_port = parser_json.upload_state_lvl2_json(cla.contro.path_config, "hubium", "sock_client_port")
    cla.hubium.http_server_port = parser_json.upload_state_lvl2_json(cla.contro.path_config, "hubium", "http_server_port")

def update_state_file():
    parser_json.update_state_lvl2_json(cla.contro.path_state_co, "self", "ip", cla.contro.ip)
    parser_json.update_state_lvl2_json(cla.contro.path_state_co, "self", "sock_server_port", cla.contro.sock_server_port)

    parser_json.update_state_lvl2_json(cla.contro.path_state_co, "hubium", "ip", cla.hubium.edge_ip)
    parser_json.update_state_lvl2_json(cla.contro.path_state_co, "hubium", "sock_client_port", cla.hubium.sock_client_port)
    parser_json.update_state_lvl2_json(cla.contro.path_state_co, "hubium", "http_server_port", cla.hubium.http_server_port)

def upload_hu_state():
    cla.hubium.status = parser_json.upload_state_lvl1_json(cla.contro.path_state_hu, "status")
    cla.hubium.ip = parser_json.upload_state_lvl1_json(cla.contro.path_state_hu, "ip")
