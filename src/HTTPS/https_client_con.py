#---------------------------------------------
from src.param import param_co
from src.HTTPS import https_client_post
from src.HTTPS import https_client_fct


# Test Hubium HTTP connection
def test_hu_con():
    ip = param_co.state_co["hubium"]["ip"]
    port = param_co.state_co["hubium"]["http_server_port"]
    connected = https_client_fct.send_https_ping(ip, port)
    if(connected):
        connection_hu_open()
    else:
        connection_hu_close()

def connection_hu_open():
    if(param_co.state_co["hubium"]["http_connected"] == False):
        param_co.state_co["hubium"]["http_connected"] = True
        https_client_post.post_param_value("hu", "controlium", "ip", param_co.state_co["self"]["ip"])
        https_client_post.post_param_value("hu", "pywardium", "ip", param_co.state_hu["pywardium"]["ip"])
        https_client_post.post_param_value("hu", "velodium", "ip", param_co.state_hu["velodium"]["ip"])
        https_client_post.post_param_value("hu", "self", "lidar_main", param_co.state_hu["self"]["lidar_main"])

def connection_hu_close():
    param_co.state_co["hubium"]["http_connected"] = False
