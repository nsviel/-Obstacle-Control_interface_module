#---------------------------------------------
from src.param import param_control
from src.element import element
from src.connection.HTTPS.client import https_client_post
from src.connection.HTTPS.client import https_client_fct


# Test module_edge HTTP connection
def test_connection_edge():
    ip = param_control.state_edge["hub"]["info"]["ip"]
    port = param_control.state_edge["hub"]["http"]["server_port"]
    connected = https_client_fct.send_https_ping(ip, port)
    param_control.state_control["interface"]["edge"]["http_connected"] = connected

    if(connected == True and test_connection_edge.edge_has_been_deco):
        test_connection_edge.edge_has_been_co = True
        test_connection_edge.edge_has_been_deco = False
        https_client_post.post_state_edge("control", param_control.state_control)
        https_client_post.post_state_edge("edge", param_control.state_edge)
        https_client_post.post_state_edge("ground", param_control.state_ground)
        terminal.addConnection("Edge", "on")
    elif(connected == False and test_connection_edge.edge_has_been_co):
        test_connection_edge.edge_has_been_co = False
        test_connection_edge.edge_has_been_deco = True
        terminal.addConnection("Edge", "off")

test_connection_edge.edge_has_been_co = False
test_connection_edge.edge_has_been_deco = True
