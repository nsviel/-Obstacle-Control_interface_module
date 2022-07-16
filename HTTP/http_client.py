#! /usr/bin/python
#---------------------------------------------

from param import param_co
from HTTP import http_client_fct
from src import parser_json


def test_connection():
    connected = http_client_fct.send_conn_request("/test_http_conn")
    if(connected):
        param_co.state_co["hubium"]["connected"] = True
    else:
        connection_closed()

def connection_closed():
    param_co.state_co["hubium"]["connected"] = False
    param_co.state_hu["sncf"]["connected"] = False
    param_co.state_hu["velodium"]["connected"] = False
    param_co.state_hu["pywardium"]["connected"] = False
