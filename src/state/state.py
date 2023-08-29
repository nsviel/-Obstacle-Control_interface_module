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
    terminal.addLog("#", "Configuration loaded")

def load_json_file():
    param_control.state_ground = parser_json.load_state(param_control.path_state_initial + "state_ground.json")
    param_control.state_edge = parser_json.load_state(param_control.path_state_initial + "state_edge.json")
    param_control.state_control = parser_json.load_state(param_control.path_state_initial + "state_control.json")
    param_control.state_network = parser_json.load_state(param_control.path_state_initial + "state_network.json")
    param_control.state_cloud = parser_json.load_state(param_control.path_state_initial + "state_cloud.json")

def upload_state():
    parser_json.upload_file(param_control.path_state_current + "state_ground.json", param_control.state_ground)
    parser_json.upload_file(param_control.path_state_current + "state_edge.json", param_control.state_edge)
    parser_json.upload_file(param_control.path_state_current + "state_control.json", param_control.state_control)
    parser_json.upload_file(param_control.path_state_current + "state_network.json", param_control.state_network)
    parser_json.upload_file(param_control.path_state_current + "state_cloud.json", param_control.state_cloud)

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
