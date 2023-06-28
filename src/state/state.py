#---------------------------------------------
from src.param import param_interface
from src.connection import connection
from src.utils import parser_json
from src.utils import wallet
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
    param_interface.state_interface = parser_json.load_state(param_interface.path_state_interface)
    param_interface.state_edge_1 = parser_json.load_state(param_interface.path_state_edge_1)
    param_interface.state_capture = parser_json.load_state(param_interface.path_state_capture)
    param_interface.state_network = parser_json.load_state(param_interface.path_state_perf)

def init_state_co():
    param_interface.state_interface["self"]["ip"] = signal.get_ip_adress()
    param_interface.state_interface["path"]["file_name_add"] = ""
    param_interface.state_interface["edge"]["http_connected"] = False

def init_state_perf():
    param_interface.state_network["mongo"]["connected"] = False

    param_interface.state_network["local_cloud"]["timestamp"] = 0
    param_interface.state_network["local_cloud"]["throughput"]["value"] = 0
    param_interface.state_network["local_cloud"]["throughput"]["min"] = 0
    param_interface.state_network["local_cloud"]["throughput"]["max"] = 0
    param_interface.state_network["local_cloud"]["throughput"]["mean"] = 0
    param_interface.state_network["local_cloud"]["latency"]["value"] = 0
    param_interface.state_network["local_cloud"]["latency"]["min"] = 0
    param_interface.state_network["local_cloud"]["latency"]["max"] = 0
    param_interface.state_network["local_cloud"]["latency"]["mean"] = 0
    param_interface.state_network["local_cloud"]["reliability"]["value"] = 0
    param_interface.state_network["local_cloud"]["reliability"]["min"] = 0
    param_interface.state_network["local_cloud"]["reliability"]["max"] = 0
    param_interface.state_network["local_cloud"]["reliability"]["mean"] = 0
    param_interface.state_network["local_cloud"]["interruption"]["value"] = 0
    param_interface.state_network["local_cloud"]["interruption"]["min"] = 0
    param_interface.state_network["local_cloud"]["interruption"]["max"] = 0
    param_interface.state_network["local_cloud"]["interruption"]["mean"] = 0

    param_interface.state_network["cloud_local"]["timestamp"] = 0
    param_interface.state_network["cloud_local"]["latency"]["value"] = 0
    param_interface.state_network["cloud_local"]["latency"]["min"] = 0
    param_interface.state_network["cloud_local"]["latency"]["max"] = 0
    param_interface.state_network["cloud_local"]["latency"]["mean"] = 0
    param_interface.state_network["cloud_local"]["reliability"]["value"] = 0
    param_interface.state_network["cloud_local"]["reliability"]["min"] = 0
    param_interface.state_network["cloud_local"]["reliability"]["max"] = 0
    param_interface.state_network["cloud_local"]["reliability"]["mean"] = 0

    param_interface.state_network["end_to_end"]["time_slam"] = 0
    param_interface.state_network["end_to_end"]["time_ai"] = 0
    param_interface.state_network["end_to_end"]["time_total"] = 0

def load_config_file():
    config = parser_json.load_data_from_file(param_interface.path_config)
    param_interface.state_interface["self"]["sock_server_l1_port"] = config["self"]["sock_server_l1_port"]
    param_interface.state_interface["self"]["sock_server_l2_port"] = config["self"]["sock_server_l2_port"]
    param_interface.tic_image = config["self"]["tic_image"]
    param_interface.tic_connection = config["self"]["tic_connection"]

    param_interface.state_interface["gui"]["width"] = config["gui"]["width"]
    param_interface.state_interface["gui"]["height"] = config["gui"]["height"]
    param_interface.state_interface["edge"]["ip"] = config["edge"]["ip"]
    param_interface.state_interface["edge"]["http_server_port"] = config["edge"]["http_server_port"]
    param_interface.state_interface["ssd"]["activated"] = config["ssd"]["start_with_save_data"]

def upload_state():
    parser_json.upload_file(param_interface.path_state_edge_1, param_interface.state_edge_1)
    parser_json.upload_file(param_interface.path_state_capture, param_interface.state_capture)
    parser_json.upload_file(param_interface.path_state_interface, param_interface.state_interface)

def update_state():
    param_interface.status_interface = "Offline"
    param_interface.status_hu = "Offline"
    param_interface.status_py = "Offline"
    param_interface.status_processing = "Offline"
    param_interface.status_ai = "Offline"
    param_interface.status_ed = "Offline"
    param_interface.status_ssd = "Offline"
    param_interface.status_operator = "Offline"
    param_interface.status_l1 = "Offline"
    param_interface.status_l2 = "Offline"
    param_interface.status_db = "Offline"

    param_interface.status_interface = "Online"
    if(param_interface.state_interface["ssd"]["connected"]):
        param_interface.status_ssd = "Online"
    if(param_interface.state_interface["edge"]["http_connected"]):
        param_interface.status_hu = "Online"
        if(param_interface.state_edge_1["module_capture"]["http_connected"]):
            param_interface.status_py = "Online"
            if(param_interface.state_capture["lidar_1"]["connected"]):
                param_interface.status_l1 = "Online"
            if(param_interface.state_capture["lidar_2"]["connected"]):
                param_interface.status_l2 = "Online"
        if(param_interface.state_edge_1["component_ai"]["http_connected"]):
            param_interface.status_ai = "Online"
        if(param_interface.state_edge_1["component_process"]["http_connected"]):
            param_interface.status_processing = "Online"
        if(param_interface.state_edge_1["edge_next"]["http_connected"]):
            param_interface.status_ed = "Online"
        if(param_interface.state_edge_1["train_operator"]["broker_connected"]):
            param_interface.status_operator = "Online"

    if(param_interface.status_hu == "Offline"):
        param_interface.state_edge_1["data"]["nb_frame"] = 0
        param_interface.state_edge_1["data"]["nb_prediction"] = 0
        param_interface.state_edge_1["self"]["nb_thread"] = 0
        param_interface.state_edge_1["train_operator"]["broker_connected"] = False
        param_interface.state_edge_1["component_ai"]["http_connected"] = False
        param_interface.state_edge_1["component_process"]["sock_connected"] = False
        param_interface.state_edge_1["component_process"]["http_connected"] = False
        param_interface.state_edge_1["module_capture"]["http_connected"] = False
        param_interface.state_edge_1["module_capture"]["sock_l1_connected"] = False
        param_interface.state_edge_1["module_capture"]["sock_l2_connected"] = False

    if(param_interface.status_py == "Offline"):
        param_interface.state_capture["self"]["nb_thread"] = 0
        param_interface.state_capture["nb_thread"] = 0
        param_interface.state_capture["device"] = {}

        param_interface.state_capture["lidar_1"]["connected"] = False
        param_interface.state_capture["lidar_1"]["activated"] = False
        param_interface.state_capture["lidar_1"]["running"] = False
        param_interface.state_capture["lidar_1"]["packet"]["value"] = 0
        param_interface.state_capture["lidar_1"]["packet"]["min"] = 0
        param_interface.state_capture["lidar_1"]["packet"]["mean"] = 0
        param_interface.state_capture["lidar_1"]["packet"]["max"] = 0
        param_interface.state_capture["lidar_1"]["throughput"]["value"] = 0
        param_interface.state_capture["lidar_1"]["throughput"]["min"] = 0
        param_interface.state_capture["lidar_1"]["throughput"]["mean"] = 0
        param_interface.state_capture["lidar_1"]["throughput"]["max"] = 0

        param_interface.state_capture["lidar_2"]["connected"] = False
        param_interface.state_capture["lidar_2"]["activated"] = False
        param_interface.state_capture["lidar_2"]["running"] = False
        param_interface.state_capture["lidar_2"]["packet"]["min"] = 0
        param_interface.state_capture["lidar_2"]["packet"]["mean"] = 0
        param_interface.state_capture["lidar_2"]["packet"]["max"] = 0
        param_interface.state_capture["lidar_2"]["throughput"]["value"] = 0
        param_interface.state_capture["lidar_2"]["throughput"]["min"] = 0
        param_interface.state_capture["lidar_2"]["throughput"]["mean"] = 0
        param_interface.state_capture["lidar_2"]["throughput"]["max"] = 0

    if(param_interface.status_processing == "Offline"):
        param_interface.state_edge_1["component_process"]["sock_connected"] = False

    if(param_interface.state_network["mongo"]["connected"]):
        param_interface.status_db = "Online"
