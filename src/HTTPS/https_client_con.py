#---------------------------------------------
from src.param import param_co
from src.HTTPS import https_client_post
from src.HTTPS import https_client_fct


# Test module_edge HTTP connection
def test_hu_con():
    ip = param_co.state_co["module_edge"]["ip"]
    port = param_co.state_co["module_edge"]["http_server_port"]
    connected = https_client_fct.send_https_ping(ip, port)
    if(connected):
        connection_hu_open()
    else:
        connection_hu_close()

def connection_hu_open():
    if(param_co.state_co["module_edge"]["http_connected"] == False):
        param_co.state_co["module_edge"]["http_connected"] = True
        https_client_post.post_param_value("hu", "module_interface", "ip", param_co.state_co["self"]["ip"])
        https_client_post.post_param_value("hu", "module_capture", "ip", param_co.state_hu["module_capture"]["ip"])
        https_client_post.post_param_value("hu", "component_process", "ip", param_co.state_hu["component_process"]["ip"])
        https_client_post.post_param_value("hu", "self", "lidar_main", param_co.state_hu["self"]["lidar_main"])

def connection_hu_close():
    param_co.state_co["module_edge"]["http_connected"] = False
