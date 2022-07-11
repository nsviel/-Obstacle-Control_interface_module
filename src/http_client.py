#! /usr/bin/python
#---------------------------------------------

from param import cla

import json
import http.client as client


def test_connection():
    if(cla.contro.http_connected == False):
        ip = cla.hubium.ip
        port = cla.hubium.http_server_port
        sock = client.HTTPConnection(ip, port, timeout=0.1)
        try:
            sock.request("GET", "/test")
            cla.contro.http_connected = True
        except:
            connection_closed()
        sock.close()

def connection_closed():
    cla.contro.http_connected = False
    cla.pyward.http_connected = False
    cla.hubium.reset()
