#! /usr/bin/python
#---------------------------------------------

from param import param_co
from param import param_hu
from param import param_py

import json
import http.client as client


def test_connection():
    if(param_co.http_connected == False):
        sock = client.HTTPConnection(param_hu.ip, param_hu.http_server_port, timeout=0.1)
        try:
            sock.request("GET", "/test")
            param_co.http_connected = True
        except:
            connection_closed()
        sock.close()

def connection_closed():
    param_co.http_connected = False
    param_py.http_connected = False
    param_hu.mqtt_connected = False
