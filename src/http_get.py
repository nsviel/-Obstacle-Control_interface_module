#! /usr/bin/python
#---------------------------------------------

from param import param_co
from classes import classes

from src import http
from src import connection
from src import parser_json

import json
import requests
import http.client as client


def get_falsealarm():
    if(param_co.http_connected):
        try:
            sock = client.HTTPConnection(classes.hubium.ip, classes.hubium.http_server_port, timeout=1)
            sock.request("GET", "/falsealarm")
            print("[#] False alarm sended")
        except:
            http.connection_closed()

def get_state():
    is_loaded = False
    if(param_co.http_connected):
        try:
            sock = client.HTTPConnection(classes.hubium.ip, classes.hubium.http_server_port, timeout=1)
            sock.request("GET", "/state")
            response = sock.getresponse()
            data = response.read()
            parser_json.upload_json_file(param_co.path_state_hu, data)
            sock.close()
            is_loaded = True
        except:
            http.connection_closed()
