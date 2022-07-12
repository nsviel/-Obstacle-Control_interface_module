#! /usr/bin/python
#---------------------------------------------

from param import param_co

from src import parser_json


def load_configuration():
    load_json_file()
    upload_config_file()

def load_json_file():
    param_co.state_co = parser_json.load_file(param_co.path_state_co)
    param_co.state_hu = parser_json.load_file(param_co.path_state_hu)
    param_co.state_py = parser_json.load_file(param_co.path_state_py)

def upload_config_file():
    config = parser_json.load_file(param_co.path_config)
    param_co.state_co["self"]["sock_server_port"] = config["self"]["sock_server_port"]
    param_co.state_co["gui"]["width"] = config["gui"]["width"]
    param_co.state_co["gui"]["height"] = config["gui"]["height"]

    param_co.state_co["hubium"]["ip"] = config["hubium"]["ip"]
    param_co.state_co["hubium"]["sock_client_port"] = config["hubium"]["sock_client_port"]
    param_co.state_co["hubium"]["http_server_port"] = config["hubium"]["http_server_port"]
