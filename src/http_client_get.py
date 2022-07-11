#! /usr/bin/python
#---------------------------------------------

from param import cla

from src import http_client
from src import connection
from src import parser_json

import json
import requests
import http.client as client


def get_falsealarm():
    if(cla.contro.http_connected):
        try:
            ip = cla.hubium.ip
            port = cla.hubium.http_server_port
            sock = client.HTTPConnection(ip, port, timeout=1)
            sock.request("GET", "/falsealarm")
            print("[#] False alarm sended")
        except:
            http_client.connection_closed()

def get_state():
    is_loaded = False
    if(cla.contro.http_connected):
        try:
            ip = cla.hubium.ip
            port = cla.hubium.http_server_port
            sock = client.HTTPConnection(ip, port, timeout=1)
            sock.request("GET", "/state_hu")
            response = sock.getresponse()
            data = response.read()
            parser_json.upload_json_file(cla.contro.path_state_hu, data)
            sock.close()
            is_loaded = True
        except:
            http_client.connection_closed()

def get_image():
    is_loaded = False
    print("get image")
    if(cla.contro.http_connected):
        try:
            ip = cla.hubium.ip
            port = cla.hubium.http_server_port
            sock = client.HTTPConnection(ip, port, timeout=1)
            sock.request("GET", "/image")
            response = sock.getresponse()
            data = response.read()
            print("data received")
            print(len(data))

            sock.close()
            is_loaded = True
        except:
            http_client.connection_closed()
