#! /usr/bin/python
#---------------------------------------------

from param import classes

from src import parser_json


def init_state():
    upload_config_file()
    update_state_file()

def upload_config_file():
    classes.contro.ip = parser_json.upload_state_lvl2_json(classes.contro.path_config, "self", "ip")
    classes.contro.port_sock_server = parser_json.upload_state_lvl2_json(classes.contro.path_config, "self", "sock_server_port")

    classes.hubium.ip = parser_json.upload_state_lvl2_json(classes.contro.path_config, "hubium", "ip")
    classes.hubium.sock_client_port = parser_json.upload_state_lvl2_json(classes.contro.path_config, "hubium", "sock_client_port")
    classes.hubium.http_server_port = parser_json.upload_state_lvl2_json(classes.contro.path_config, "hubium", "http_server_port")

def update_state_file():
    parser_json.update_state_lvl2_json(classes.contro.path_state_co, "self", "ip", classes.contro.ip)
    parser_json.update_state_lvl2_json(classes.contro.path_state_co, "self", "sock_server_port", classes.contro.sock_server_port)

    parser_json.update_state_lvl2_json(classes.contro.path_state_co, "hubium", "ip", classes.hubium.edge_ip)
    parser_json.update_state_lvl2_json(classes.contro.path_state_co, "hubium", "sock_client_port", classes.hubium.sock_client_port)
    parser_json.update_state_lvl2_json(classes.contro.path_state_co, "hubium", "http_server_port", classes.hubium.http_server_port)

def upload_hu_state():
    classes.hubium.status = parser_json.upload_state_lvl1_json(classes.contro.path_state_hu, "status")
    classes.hubium.ip = parser_json.upload_state_lvl1_json(classes.contro.path_state_hu, "ip")
