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
    upload_state()
    terminal.addLog("#", "Configuration loaded")

def load_json_file():
    param_control.state_ground = parser_json.load_state(param_control.path_state_initial + "state_ground.json")
    param_control.state_edge = parser_json.load_state(param_control.path_state_initial + "state_edge.json")
    param_control.state_control = parser_json.load_state(param_control.path_state_initial + "state_control.json")
    param_control.state_network = parser_json.load_state(param_control.path_state_initial + "state_network.json")
    param_control.state_cloud = parser_json.load_state(param_control.path_state_initial + "state_cloud.json")

def init_state_co():
    param_control.state_control["control"]["ip"] = signal.get_ip_adress()
    param_control.state_control["ssd"]["path"]["file_name_add"] = ""
    param_control.state_edge["hub"]["http"]["connected"] = False

def init_state_perf():
    param_control.state_network["mongodb"]["connected"] = False

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

    param_control.state_network["time"]["slam"] = 0
    param_control.state_network["time"]["ai"] = 0
    param_control.state_network["time"]["total"] = 0

def upload_state():
    parser_json.upload_file(param_control.path_state_current + "state_edge.json", param_control.state_edge)
    parser_json.upload_file(param_control.path_state_current + "state_ground.json", param_control.state_ground)
    parser_json.upload_file(param_control.path_state_current + "state_control.json", param_control.state_control)

def update_state():
    param_control.status_control = "Offline"
    param_control.status_edge = "Offline"
    param_control.status_capture = "Offline"
    param_control.status_slam = "Offline"
    param_control.status_ai = "Offline"
    param_control.status_ssd = "Offline"
    param_control.status_operator = "Offline"
    param_control.status_lidar_1 = "Offline"
    param_control.status_lidar_2 = "Offline"
    param_control.status_db = "Offline"

    param_control.status_control = "Online"
    if(param_control.state_control["ssd"]["connected"]):
        param_control.status_ssd = "Online"

    if(param_control.state_edge["hub"]["http"]["connected"]):
        param_control.status_edge = "Online"
        if(param_control.state_ground["capture"]["http_connected"]):
            param_control.status_capture = "Online"
            if(param_control.state_ground["lidar_1"]["connected"]):
                param_control.status_lidar_1 = "Online"
            if(param_control.state_ground["lidar_2"]["connected"]):
                param_control.status_lidar_2 = "Online"
        if(param_control.state_edge["ai"]["http_connected"]):
            param_control.status_ai = "Online"
        if(param_control.state_edge["slam"]["http_connected"]):
            param_control.status_slam = "Online"
        if(param_control.state_cloud["operator"]["broker_connected"]):
            param_control.status_operator = "Online"

    if(param_control.status_edge == "Offline"):
        param_control.state_edge["data"]["nb_frame"] = 0
        param_control.state_edge["data"]["nb_prediction"] = 0
        param_control.state_edge["hub"]["nb_thread"] = 0
        param_control.state_cloud["operator"]["broker_connected"] = False
        param_control.state_edge["ai"]["http_connected"] = False
        param_control.state_edge["slam"]["sock_connected"] = False
        param_control.state_edge["slam"]["http_connected"] = False
        param_control.state_ground["capture"]["http_connected"] = False
        param_control.state_ground["capture"]["sock_l1_connected"] = False
        param_control.state_ground["capture"]["sock_l2_connected"] = False

    if(param_control.status_capture == "Offline"):
        param_control.state_ground["capture"]["nb_thread"] = 0
        param_control.state_ground["nb_thread"] = 0

        param_control.state_ground["lidar_1"]["connected"] = False
        param_control.state_ground["lidar_1"]["activated"] = False
        param_control.state_ground["lidar_1"]["running"] = False
        param_control.state_ground["lidar_1"]["packet"]["value"] = 0
        param_control.state_ground["lidar_1"]["packet"]["min"] = 0
        param_control.state_ground["lidar_1"]["packet"]["mean"] = 0
        param_control.state_ground["lidar_1"]["packet"]["max"] = 0
        param_control.state_ground["lidar_1"]["throughput"]["value"] = 0
        param_control.state_ground["lidar_1"]["throughput"]["min"] = 0
        param_control.state_ground["lidar_1"]["throughput"]["mean"] = 0
        param_control.state_ground["lidar_1"]["throughput"]["max"] = 0

        param_control.state_ground["lidar_2"]["connected"] = False
        param_control.state_ground["lidar_2"]["activated"] = False
        param_control.state_ground["lidar_2"]["running"] = False
        param_control.state_ground["lidar_2"]["packet"]["min"] = 0
        param_control.state_ground["lidar_2"]["packet"]["mean"] = 0
        param_control.state_ground["lidar_2"]["packet"]["max"] = 0
        param_control.state_ground["lidar_2"]["throughput"]["value"] = 0
        param_control.state_ground["lidar_2"]["throughput"]["min"] = 0
        param_control.state_ground["lidar_2"]["throughput"]["mean"] = 0
        param_control.state_ground["lidar_2"]["throughput"]["max"] = 0

    if(param_control.status_slam == "Offline"):
        param_control.state_edge["slam"]["sock_connected"] = False

    if(param_control.state_network["mongodb"]["connected"]):
        param_control.status_db = "Online"
