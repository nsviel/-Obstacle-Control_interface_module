#! /usr/bin/python
#---------------------------------------------

from param import param_co
from param import param_hu
from param import param_py

import json
import http.client as client


def test_connection():
    sock = client.HTTPConnection(param_hu.hubium_ip, param_hu.hubium_httpd_port, timeout=0.1)
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
