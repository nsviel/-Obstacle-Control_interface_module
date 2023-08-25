#---------------------------------------------
from src.param import param_control
from src.element import element
from src.connection.HTTPS import https_client_post
from src.connection.HTTPS import https_client_fct


# Test module_edge HTTP connection
def test_connection_edge():
    test_http_edge("edge_1")
    test_http_edge("edge_2")

def test_http_edge(edge_ID):
    state = param_control.state.cloud.interface[edge_ID]
    ip = state["ip"]
    port = state["http"]["port_server"]
    connected = https_client_fct.send_https_ping(ip, port)
    if(connected):
        connection_edge_open(edge_ID)
    else:
        connection_edge_close(edge_ID)

def connection_edge_open(edge_ID):
    state_edge = element.object.cloud.state.state_interface[edge_ID]
    state_control = element.object.cloud.state.state_component["control"]
    state_ground = element.object.ground.state.state_component["control"]
    if(state_edge["http"]["connected"] == False):
        state_edge["http"]["connected"] = True
        https_client_post.post_param_value("edge", "module_interface", "ip", state_control["ip"])
        https_client_post.post_param_value("edge", "module_capture", "ip", param_control.state_edge_1["module_capture"]["ip"])
        https_client_post.post_param_value("edge", "component_process", "ip", param_control.state_edge_1["component_process"]["ip"])
        https_client_post.post_param_value("edge", "self", "lidar_main", param_control.state_edge_1["self"]["lidar_main"])

def connection_edge_close():
    param_control.state_control["edge_1"]["http_connected"] = False
