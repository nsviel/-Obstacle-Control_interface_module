#! /usr/bin/python
#---------------------------------------------

from param import param_co
from src import connection
from src import parser_json


def load_configuration():
    load_json_file()
    init_state()
    load_config_file()
    upload_state()

def load_json_file():
    param_co.state_co = parser_json.load_file(param_co.path_state_co)
    param_co.state_hu = parser_json.load_file(param_co.path_state_hu)
    param_co.state_py = parser_json.load_file(param_co.path_state_py)

def init_state():
    param_co.state_co["self"]["ip"] = connection.get_ip_adress()

    param_co.state_hu["self"]["status"] = "Offline"
    param_co.state_hu["self"]["ip"] = "127.0.0.1"
    param_co.state_hu["self"]["nb_frame"] = 0
    param_co.state_hu["self"]["nb_prediction"] = 0
    param_co.state_hu["self"]["nb_thread"] = 0
    param_co.state_hu["sncf"]["broker_connected"] = False
    param_co.state_hu["ai"]["http_connected"] = False
    param_co.state_hu["velodium"]["sock_connected"] = False

    param_co.state_py["self"]["status"] = "Offline"
    param_co.state_py["self"]["nb_thread"] = 0
    param_co.state_py["lidar_1"]["connected"] = False
    param_co.state_py["lidar_1"]["nb_packet"] = 0
    param_co.state_py["lidar_1"]["bandwidth"] = 0
    param_co.state_py["lidar_2"]["connected"] = False
    param_co.state_py["lidar_2"]["nb_packet"] = 0
    param_co.state_py["lidar_2"]["bandwidth"] = 0
    param_co.state_py["device"] = {}

def load_config_file():
    config = parser_json.load_file(param_co.path_config)
    param_co.state_co["self"]["sock_server_port"] = config["self"]["sock_server_port"]
    param_co.state_co["gui"]["width"] = config["gui"]["width"]
    param_co.state_co["gui"]["height"] = config["gui"]["height"]

    param_co.state_co["hubium"]["ip"] = config["hubium"]["ip"]
    param_co.state_co["hubium"]["sock_client_port"] = config["hubium"]["sock_client_port"]
    param_co.state_co["hubium"]["http_server_port"] = config["hubium"]["http_server_port"]

def upload_state():
    parser_json.upload_file(param_co.path_state_hu, param_co.state_hu)
    parser_json.upload_file(param_co.path_state_py, param_co.state_py)
    parser_json.upload_file(param_co.path_state_co, param_co.state_co)
