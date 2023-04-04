#---------------------------------------------
from src.param import param_interface
from src.HTTPS import https_client_post
from src.HTTPS import https_client_fct


# Test module_edge HTTP connection
def test_edge_con():
    ip = param_interface.state_interface["edge"]["ip"]
    port = param_interface.state_interface["edge"]["http_server_port"]
    connected = https_client_fct.send_https_ping(ip, port)
    if(connected):
        connection_edge_open()
    else:
        connection_edge_close()

def connection_edge_open():
    if(param_interface.state_interface["edge"]["http_connected"] == False):
        param_interface.state_interface["edge"]["http_connected"] = True
        https_client_post.post_param_value("edge", "module_interface", "ip", param_interface.state_interface["self"]["ip"])
        https_client_post.post_param_value("edge", "module_capture", "ip", param_interface.state_edge["module_capture"]["ip"])
        https_client_post.post_param_value("edge", "component_process", "ip", param_interface.state_edge["component_process"]["ip"])
        https_client_post.post_param_value("edge", "self", "lidar_main", param_interface.state_edge["self"]["lidar_main"])

def connection_edge_close():
    param_interface.state_interface["edge"]["http_connected"] = False
