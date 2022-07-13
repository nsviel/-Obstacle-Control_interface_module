#! /usr/bin/python
#---------------------------------------------

from param import param_co
from src import parser_json

import json
import http.client as client


def test_connection():
    connected = param_co.state_co["hubium"]["connected"]
    ip = param_co.state_co["hubium"]["ip"]
    port = param_co.state_co["hubium"]["http_server_port"]
    if(connected == False):
        sock = client.HTTPConnection(ip, port, timeout=0.1)
        try:
            sock.request("GET", "/test_http_conn")
            param_co.state_co["hubium"]["connected"] = True
        except:
            connection_closed()
        sock.close()

def connection_closed():
    param_co.state_co["hubium"]["connected"] = False
    param_co.state_hu["sncf"]["connected"] = False
    param_co.state_hu["velodium"]["connected"] = False
    param_co.state_hu["pywardium"]["connected"] = False
    parser_json.upload_file(param_co.path_state_co, param_co.state_co)
