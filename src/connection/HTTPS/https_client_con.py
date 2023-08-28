#---------------------------------------------
from src.param import param_control
from src.element import element
from src.connection.HTTPS import https_client_post
from src.connection.HTTPS import https_client_fct


# Test module_edge HTTP connection
def test_connection_edge():
    ip = param_control.state_control["edge"]["ip"]
    port = param_control.state_control["edge"]["http_server_port"]
    connected = https_client_fct.send_https_ping(ip, port)
    if(connected):
        connection_edge_open()
    else:
        connection_edge_close()

def connection_edge_open():
    if(param_control.state_control["edge"]["http_connected"] == False):
        param_control.state_control["edge"]["http_connected"] = True
        https_client_post.post_param_value("edge", "module_interface", "ip", param_control.state_control["self"]["ip"])
        https_client_post.post_param_value("edge", "module_capture", "ip", param_control.state_edge["module_capture"]["ip"])
        https_client_post.post_param_value("edge", "slam", "ip", param_control.state_edge["slam"]["ip"])
        https_client_post.post_param_value("edge", "self", "lidar_main", param_control.state_edge["self"]["lidar_main"])

def connection_edge_close():
    param_control.state_control["edge"]["http_connected"] = False
