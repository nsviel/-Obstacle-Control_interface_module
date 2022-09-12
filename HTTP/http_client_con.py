#! /usr/bin/python
#---------------------------------------------

from param import param_co
from HTTP import http_client_post

import http.client


#-----------------------
# Test Hubium HTTP connection
def test_hu_con():
    ip = param_co.state_co["hubium"]["ip"]
    port = param_co.state_co["hubium"]["http_server_port"]
    client = http.client.HTTPConnection(ip, port, timeout=0.1)
    try:
        client.request("GET", "/test_http_conn")
        connection_hu_open()
    except:
        connection_hu_close()
    client.close()
def connection_hu_open():
    connected = param_co.state_co["hubium"]["http_connected"]
    if(connected == False):
        param_co.state_co["hubium"]["http_connected"] = True
        param_co.state_hu["controlium"]["ip"] = param_co.state_co["self"]["ip"]
        http_client_post.post_param_hu("controlium", "ip", param_co.state_co["self"]["ip"])
def connection_hu_close():
    param_co.state_hu["self"]["status"] = "Offline"
    param_co.state_hu["edge"]["status"] = "Offline"
    param_co.state_hu["ai"]["status"] = "Offline"
    param_co.state_hu["velodium"]["status"] = "Offline"
    param_co.state_py["self"]["status"] = "Offline"
    param_co.state_hu["edge"]["http_connected"] = False
    param_co.state_co["hubium"]["http_connected"] = False
    param_co.state_co["hubium"]["sock_l1_connected"] = False
    param_co.state_co["hubium"]["sock_l2_connected"] = False
    param_co.state_hu["sncf"]["broker_connected"] = False
    param_co.state_hu["velodium"]["sock_connected"] = False
    param_co.state_hu["pywardium"]["http_connected"] = False
    param_co.state_hu["pywardium"]["sock_l1_connected"] = False
    param_co.state_hu["pywardium"]["sock_l2_connected"] = False
