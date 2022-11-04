#---------------------------------------------
from param import param_co
from src import connection
from src import parser_json
from src import wallet
from src import network


def load_configuration():
    load_json_file()
    init_state()
    load_config_file()
    upload_state()

def load_json_file():
    param_co.state_co = parser_json.load_data_from_file(param_co.path_state_co)
    param_co.state_hu = parser_json.load_data_from_file(param_co.path_state_hu)
    param_co.state_py = parser_json.load_data_from_file(param_co.path_state_py)
    param_co.state_perf = parser_json.load_data_from_file(param_co.path_state_perf)

def init_state():
    param_co.state_co["self"]["ip"] = network.get_ip_adress()
    param_co.state_co["path"]["file_name_add"] = ""

def load_config_file():
    config = parser_json.load_data_from_file(param_co.path_config)
    param_co.state_co["self"]["sock_server_l1_port"] = config["self"]["sock_server_l1_port"]
    param_co.state_co["self"]["sock_server_l2_port"] = config["self"]["sock_server_l2_port"]
    param_co.state_co["gui"]["width"] = config["gui"]["width"]
    param_co.state_co["gui"]["height"] = config["gui"]["height"]
    param_co.state_co["hubium"]["ip"] = config["hubium"]["ip"]
    param_co.state_co["hubium"]["http_server_port"] = config["hubium"]["http_server_port"]

def upload_state():
    parser_json.upload_file(param_co.path_state_hu, param_co.state_hu)
    parser_json.upload_file(param_co.path_state_py, param_co.state_py)
    parser_json.upload_file(param_co.path_state_co, param_co.state_co)

def update_state():
    param_co.status_co = "Offline"
    param_co.status_hu = "Offline"
    param_co.status_py = "Offline"
    param_co.status_ve = "Offline"
    param_co.status_ai = "Offline"
    param_co.status_ed = "Offline"
    param_co.status_ssd = "Offline"
    param_co.status_sncf = "Offline"
    param_co.status_l1 = "Offline"
    param_co.status_l2 = "Offline"

    param_co.status_co = "Online"
    if(param_co.state_co["ssd"]["connected"]):
        param_co.status_ssd = "Online"
    if(param_co.state_co["hubium"]["http_connected"]):
        param_co.status_hu = "Online"
        if(param_co.state_hu["pywardium"]["http_connected"]):
            param_co.status_py = "Online"
            if(param_co.state_py["lidar_1"]["connected"]):
                param_co.status_l1 = "Online"
            if(param_co.state_py["lidar_2"]["connected"]):
                param_co.status_l2 = "Online"
        if(param_co.state_hu["ai"]["http_connected"]):
            param_co.status_ai = "Online"
        if(param_co.state_hu["velodium"]["http_connected"]):
            param_co.status_ve = "Online"
        if(param_co.state_hu["edge"]["http_connected"]):
            param_co.status_ed = "Online"
        if(param_co.state_hu["sncf"]["broker_connected"]):
            param_co.status_sncf = "Online"

    if(param_co.status_hu == "Offline"):
        param_co.state_hu["data"]["nb_frame"] = 0
        param_co.state_hu["data"]["nb_prediction"] = 0
        param_co.state_hu["self"]["nb_thread"] = 0
        param_co.state_hu["sncf"]["broker_connected"] = False
        param_co.state_hu["ai"]["http_connected"] = False
        param_co.state_hu["velodium"]["sock_connected"] = False
        param_co.state_hu["velodium"]["http_connected"] = False
        param_co.state_hu["pywardium"]["http_connected"] = False
        param_co.state_hu["pywardium"]["sock_l1_connected"] = False
        param_co.state_hu["pywardium"]["sock_l2_connected"] = False

    if(param_co.status_py == "Offline"):
        param_co.state_py["self"]["nb_thread"] = 0
        param_co.state_py["nb_thread"] = 0
        param_co.state_py["device"] = {}

        param_co.state_py["lidar_1"]["connected"] = False
        param_co.state_py["lidar_1"]["packet"]["value"] = 0
        param_co.state_py["lidar_1"]["packet"]["min"] = 0
        param_co.state_py["lidar_1"]["packet"]["mean"] = 0
        param_co.state_py["lidar_1"]["packet"]["max"] = 0
        param_co.state_py["lidar_1"]["throughput"]["value"] = 0
        param_co.state_py["lidar_1"]["throughput"]["min"] = 0
        param_co.state_py["lidar_1"]["throughput"]["mean"] = 0
        param_co.state_py["lidar_1"]["throughput"]["max"] = 0

        param_co.state_py["lidar_2"]["connected"] = False
        param_co.state_py["lidar_2"]["packet"]["min"] = 0
        param_co.state_py["lidar_2"]["packet"]["mean"] = 0
        param_co.state_py["lidar_2"]["packet"]["max"] = 0
        param_co.state_py["lidar_2"]["throughput"]["value"] = 0
        param_co.state_py["lidar_2"]["throughput"]["min"] = 0
        param_co.state_py["lidar_2"]["throughput"]["mean"] = 0
        param_co.state_py["lidar_2"]["throughput"]["max"] = 0

    if(param_co.status_ve == "Offline"):
        param_co.state_hu["velodium"]["sock_connected"] = False
