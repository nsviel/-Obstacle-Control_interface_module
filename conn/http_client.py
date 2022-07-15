#! /usr/bin/python
#---------------------------------------------

from param import param_co
from src import parser_json

import json
import http.client as client


def test_connection():
    ip = param_co.state_co["hubium"]["ip"]
    port = param_co.state_co["hubium"]["http_server_port"]

    connected = http_connection(ip, port, "/test_http_conn")
    if(connected):
        param_co.state_co["hubium"]["connected"] = True
    else:
        connection_closed()

def http_connection(ip, port, get):
    connected = False
    sock = client.HTTPConnection(ip, port, timeout=0.1)
    try:
        sock.request("GET", get)
        connected = True
    except:
        connected = False
    sock.close()
    return connected

def connection_closed():
    param_co.state_co["hubium"]["connected"] = False
    param_co.state_hu["sncf"]["connected"] = False
    param_co.state_hu["velodium"]["connected"] = False
    param_co.state_hu["pywardium"]["connected"] = False
    parser_json.upload_file(param_co.path_state_co, param_co.state_co)
