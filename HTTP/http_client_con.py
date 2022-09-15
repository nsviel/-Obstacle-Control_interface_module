#! /usr/bin/python
#---------------------------------------------

from param import param_co
from HTTP import http_client_post
from HTTP import http_client_fct


# Test Hubium HTTP connection
def test_hu_con():
    ip = param_co.state_co["hubium"]["ip"]
    port = param_co.state_co["hubium"]["http_server_port"]
    connected = http_client_fct.send_http_ping(ip, port)
    if(connected):
        connection_hu_open()
    else:
        connection_hu_close()

def connection_hu_open():
    if(param_co.state_co["hubium"]["http_connected"] == False):
        param_co.state_co["hubium"]["http_connected"] = True
        http_client_post.post_param_value("hu", "controlium", "ip", param_co.state_co["self"]["ip"])

def connection_hu_close():
    param_co.state_co["hubium"]["http_connected"] = False
