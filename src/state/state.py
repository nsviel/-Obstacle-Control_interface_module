#---------------------------------------------
from src.param import param_control
from src.utils import parser_json
from src.utils import signal
from src.utils import terminal


def load_state_initial():
    load_json_file()
    terminal.addLog("#", "Configuration loaded")

def load_json_file():
    param_control.state_ground = parser_json.load_state(param_control.path_state_initial + "state_ground.json")
    param_control.state_edge = parser_json.load_state(param_control.path_state_initial + "state_edge.json")
    param_control.state_control = parser_json.load_state(param_control.path_state_initial + "state_control.json")
    param_control.state_network = parser_json.load_state(param_control.path_state_initial + "state_network.json")
    param_control.state_cloud = parser_json.load_state(param_control.path_state_initial + "state_cloud.json")
    param_control.state_control["control"]["info"]["ip"] = signal.get_ip_adress()

def upload_state():
    parser_json.upload_file(param_control.path_state_current + "state_ground.json", param_control.state_ground)
    parser_json.upload_file(param_control.path_state_current + "state_edge.json", param_control.state_edge)
    parser_json.upload_file(param_control.path_state_current + "state_control.json", param_control.state_control)
    parser_json.upload_file(param_control.path_state_current + "state_network.json", param_control.state_network)
    parser_json.upload_file(param_control.path_state_current + "state_cloud.json", param_control.state_cloud)
