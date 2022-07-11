#! /usr/bin/python
#---------------------------------------------

from param import param_co
from param import classes

import json
import http.client as client


def test_connection():
    if(param_co.http_connected == False):
        ip = classes.hubium.ip
        port = classes.hubium.http_server_port
        sock = client.HTTPConnection(ip, port, timeout=0.1)
        try:
            sock.request("GET", "/test")
            param_co.http_connected = True
        except:
            connection_closed()
        sock.close()

def connection_closed():
    param_co.http_connected = False
    classes.pyward.http_connected = False
    classes.hubium.reset()
