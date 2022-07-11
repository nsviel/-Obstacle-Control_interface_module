#! /usr/bin/python
#---------------------------------------------

from param import classes

from src import http
from src import connection
from src import parser_json

import json
import requests
import http.client as client


def get_falsealarm():
    if(classes.contro.http_connected):
        try:
            ip = classes.hubium.ip
            port = classes.hubium.http_server_port
            sock = client.HTTPConnection(ip, port, timeout=1)
            sock.request("GET", "/falsealarm")
            print("[#] False alarm sended")
        except:
            http.connection_closed()

def get_state():
    is_loaded = False
    if(classes.contro.http_connected):
        try:
            ip = classes.hubium.ip
            port = classes.hubium.http_server_port
            sock = client.HTTPConnection(ip, port, timeout=1)
            sock.request("GET", "/state")
            response = sock.getresponse()
            data = response.read()
            parser_json.upload_json_file(classes.contro.path_state_hu, data)
            sock.close()
            is_loaded = True
        except:
            http.connection_closed()

def get_image():
    is_loaded = False
    print("get image")
    if(classes.contro.http_connected):
        try:
            ip = classes.hubium.ip
            port = classes.hubium.http_server_port
            sock = client.HTTPConnection(ip, port, timeout=1)
            sock.request("GET", "/image")
            response = sock.getresponse()
            data = response.read()
            print("data received")
            print(len(data))

            sock.close()
            is_loaded = True
        except:
            http.connection_closed()
