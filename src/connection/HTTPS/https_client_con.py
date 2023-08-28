#---------------------------------------------
from src.param import param_control
from src.element import element
from src.connection.HTTPS import https_client_post
from src.connection.HTTPS import https_client_fct


# Test module_edge HTTP connection
def test_connection_edge():
    ip = param_control.state_edge["component"]["hub"]["info"]["ip"]
    port = param_control.state_edge["component"]["hub"]["http"]["server_port"]
    connected = https_client_fct.send_https_ping(ip, port)
    if(connected):
        connection_edge_open()
    else:
        connection_edge_close()

def connection_edge_open():
    if(param_control.state_edge["component"]["hub"]["http"]["connected"] == False):
        param_control.state_edge["component"]["hub"]["http"]["connected"] = True
        https_client_post.post_state("edge", param_control.state_control)
        https_client_post.post_state("edge", param_control.state_edge)
        https_client_post.post_state("edge", param_control.state_capture)

def connection_edge_close():
    param_control.state_edge["component"]["hub"]["http"]["connected"] = False
