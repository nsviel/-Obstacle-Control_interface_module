#---------------------------------------------
from src.param import param_control
from src.connection import connection
from src.utils import parser_json
from src.element.misc.wallet import wallet_logic
from src.utils import signal
from src.utils import terminal


def load_configuration():
    load_json_file()
    init_state_co()
    init_state_perf()
    load_config_file()
    upload_state()
    terminal.addLog("#", "Configuration loaded")

def load_json_file():
    param_control.state_capture = parser_json.load_state(param_control.path_state_capture)
    param_control.state_edge_1 = parser_json.load_state(param_control.path_state_edge_1)
    param_control.state_edge_2 = parser_json.load_state(param_control.path_state_edge_2)
    param_control.state_control = parser_json.load_state(param_control.path_state_control)
    param_control.state_network = parser_json.load_state(param_control.path_state_perf)

def init_state_co():
    param_control.state_control["self"]["ip"] = signal.get_ip_adress()
    param_control.state_control["path"]["file_name_add"] = ""
    param_control.state_control["edge_1"]["http_connected"] = False

def init_state_perf():
    param_control.state_network["mongo"]["connected"] = False

    param_control.state_network["local_cloud"]["timestamp"] = 0
    param_control.state_network["local_cloud"]["throughput"]["value"] = 0
    param_control.state_network["local_cloud"]["throughput"]["min"] = 0
    param_control.state_network["local_cloud"]["throughput"]["max"] = 0
    param_control.state_network["local_cloud"]["throughput"]["mean"] = 0
    param_control.state_network["local_cloud"]["latency"]["value"] = 0
    param_control.state_network["local_cloud"]["latency"]["min"] = 0
    param_control.state_network["local_cloud"]["latency"]["max"] = 0
    param_control.state_network["local_cloud"]["latency"]["mean"] = 0
    param_control.state_network["local_cloud"]["reliability"]["value"] = 0
    param_control.state_network["local_cloud"]["reliability"]["min"] = 0
    param_control.state_network["local_cloud"]["reliability"]["max"] = 0
    param_control.state_network["local_cloud"]["reliability"]["mean"] = 0
    param_control.state_network["local_cloud"]["interruption"]["value"] = 0
    param_control.state_network["local_cloud"]["interruption"]["min"] = 0
    param_control.state_network["local_cloud"]["interruption"]["max"] = 0
    param_control.state_network["local_cloud"]["interruption"]["mean"] = 0

    param_control.state_network["cloud_local"]["timestamp"] = 0
    param_control.state_network["cloud_local"]["latency"]["value"] = 0
    param_control.state_network["cloud_local"]["latency"]["min"] = 0
    param_control.state_network["cloud_local"]["latency"]["max"] = 0
    param_control.state_network["cloud_local"]["latency"]["mean"] = 0
    param_control.state_network["cloud_local"]["reliability"]["value"] = 0
    param_control.state_network["cloud_local"]["reliability"]["min"] = 0
    param_control.state_network["cloud_local"]["reliability"]["max"] = 0
    param_control.state_network["cloud_local"]["reliability"]["mean"] = 0

    param_control.state_network["end_to_end"]["time_slam"] = 0
    param_control.state_network["end_to_end"]["time_ai"] = 0
    param_control.state_network["end_to_end"]["time_total"] = 0

def load_config_file():
    config = parser_json.load_data_from_file(param_control.path_config)
    param_control.state_control["self"]["sock_server_l1_port"] = config["self"]["sock_server_l1_port"]
    param_control.state_control["self"]["sock_server_l2_port"] = config["self"]["sock_server_l2_port"]
    param_control.tic_image = config["self"]["tic_image"]
    param_control.tic_connection = config["self"]["tic_connection"]

    param_control.state_control["gui"]["width"] = config["gui"]["width"]
    param_control.state_control["gui"]["height"] = config["gui"]["height"]
    param_control.state_control["ssd"]["activated"] = config["ssd"]["start_with_save_data"]

    param_control.state_control["edge_1"]["edge_id"] = config["edge_1"]["edge_id"]
    param_control.state_control["edge_1"]["country"] = config["edge_1"]["country"]
    param_control.state_control["edge_1"]["ip"] = config["edge_1"]["ip"]
    param_control.state_control["edge_1"]["http_server_port"] = config["edge_1"]["http_server_port"]

    param_control.state_control["edge_2"]["edge_id"] = config["edge_2"]["edge_id"]
    param_control.state_control["edge_2"]["country"] = config["edge_2"]["country"]
    param_control.state_control["edge_2"]["ip"] = config["edge_2"]["ip"]
    param_control.state_control["edge_2"]["http_server_port"] = config["edge_2"]["http_server_port"]

def upload_state():
    parser_json.upload_file(param_control.path_state_edge_1, param_control.state_edge_1)
    parser_json.upload_file(param_control.path_state_edge_2, param_control.state_edge_2)
    parser_json.upload_file(param_control.path_state_capture, param_control.state_capture)
    parser_json.upload_file(param_control.path_state_control, param_control.state_control)

def update_state():
    param_control.status_control = "Offline"
    param_control.status_edge_1 = "Offline"
    param_control.status_edge_2 = "Offline"
    param_control.status_capture = "Offline"
    param_control.status_processing = "Offline"
    param_control.status_ai = "Offline"
    param_control.status_ssd = "Offline"
    param_control.status_operator = "Offline"
    param_control.status_lidar_1 = "Offline"
    param_control.status_lidar_2 = "Offline"
    param_control.status_db = "Offline"

    param_control.status_control = "Online"
    if(param_control.state_control["ssd"]["connected"]):
        param_control.status_ssd = "Online"

    if(param_control.state_control["edge_1"]["http_connected"]):
        param_control.status_edge_1 = "Online"
        if(param_control.state_edge_1["module_capture"]["http_connected"]):
            param_control.status_capture = "Online"
            if(param_control.state_capture["lidar_1"]["connected"]):
                param_control.status_lidar_1 = "Online"
            if(param_control.state_capture["lidar_2"]["connected"]):
                param_control.status_lidar_2 = "Online"
        if(param_control.state_edge_1["component_ai"]["http_connected"]):
            param_control.status_ai = "Online"
        if(param_control.state_edge_1["component_process"]["http_connected"]):
            param_control.status_processing = "Online"
        if(param_control.state_edge_1["cloud_operator"]["broker_connected"]):
            param_control.status_operator = "Online"

    if(param_control.status_edge_1 == "Offline"):
        param_control.state_edge_1["data"]["nb_frame"] = 0
        param_control.state_edge_1["data"]["nb_prediction"] = 0
        param_control.state_edge_1["self"]["nb_thread"] = 0
        param_control.state_edge_1["cloud_operator"]["broker_connected"] = False
        param_control.state_edge_1["component_ai"]["http_connected"] = False
        param_control.state_edge_1["component_process"]["sock_connected"] = False
        param_control.state_edge_1["component_process"]["http_connected"] = False
        param_control.state_edge_1["module_capture"]["http_connected"] = False
        param_control.state_edge_1["module_capture"]["sock_l1_connected"] = False
        param_control.state_edge_1["module_capture"]["sock_l2_connected"] = False

    if(param_control.status_edge_2 == "Offline"):
        param_control.state_edge_2["data"]["nb_frame"] = 0
        param_control.state_edge_2["data"]["nb_prediction"] = 0
        param_control.state_edge_2["self"]["nb_thread"] = 0
        param_control.state_edge_2["cloud_operator"]["broker_connected"] = False
        param_control.state_edge_2["component_ai"]["http_connected"] = False
        param_control.state_edge_2["component_process"]["sock_connected"] = False
        param_control.state_edge_2["component_process"]["http_connected"] = False
        param_control.state_edge_2["module_capture"]["http_connected"] = False
        param_control.state_edge_2["module_capture"]["sock_l1_connected"] = False
        param_control.state_edge_2["module_capture"]["sock_l2_connected"] = False

    if(param_control.status_capture == "Offline"):
        param_control.state_capture["self"]["nb_thread"] = 0
        param_control.state_capture["nb_thread"] = 0
        param_control.state_capture["device"] = {}

        param_control.state_capture["lidar_1"]["connected"] = False
        param_control.state_capture["lidar_1"]["activated"] = False
        param_control.state_capture["lidar_1"]["running"] = False
        param_control.state_capture["lidar_1"]["packet"]["value"] = 0
        param_control.state_capture["lidar_1"]["packet"]["min"] = 0
        param_control.state_capture["lidar_1"]["packet"]["mean"] = 0
        param_control.state_capture["lidar_1"]["packet"]["max"] = 0
        param_control.state_capture["lidar_1"]["throughput"]["value"] = 0
        param_control.state_capture["lidar_1"]["throughput"]["min"] = 0
        param_control.state_capture["lidar_1"]["throughput"]["mean"] = 0
        param_control.state_capture["lidar_1"]["throughput"]["max"] = 0

        param_control.state_capture["lidar_2"]["connected"] = False
        param_control.state_capture["lidar_2"]["activated"] = False
        param_control.state_capture["lidar_2"]["running"] = False
        param_control.state_capture["lidar_2"]["packet"]["min"] = 0
        param_control.state_capture["lidar_2"]["packet"]["mean"] = 0
        param_control.state_capture["lidar_2"]["packet"]["max"] = 0
        param_control.state_capture["lidar_2"]["throughput"]["value"] = 0
        param_control.state_capture["lidar_2"]["throughput"]["min"] = 0
        param_control.state_capture["lidar_2"]["throughput"]["mean"] = 0
        param_control.state_capture["lidar_2"]["throughput"]["max"] = 0

    if(param_control.status_processing == "Offline"):
        param_control.state_edge_1["component_process"]["sock_connected"] = False

    if(param_control.state_network["mongo"]["connected"]):
        param_control.status_db = "Online"
