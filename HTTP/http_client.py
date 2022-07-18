#! /usr/bin/python
#---------------------------------------------

from param import param_co
from HTTP import http_client_fct
from src import parser_json
from src import connection


def test_connection():
    connected = http_client_fct.send_conn_request("/test_http_conn")
    if(connected):
        param_co.state_co["hubium"]["http_connected"] = True
    else:
        connection.connection_closed()
