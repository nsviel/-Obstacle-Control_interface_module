#! /usr/bin/python
#---------------------------------------------

from param import param_co

from src import http_client
from src import connection
from src import parser_json

import json
import requests
import http.client as client


def get_falsealarm():
    connected = param_co.state_co["hubium"]["connected"]
    ip = param_co.state_co["hubium"]["ip"]
    port = param_co.state_co["hubium"]["http_server_port"]
    if(connected):
        try:
            sock = client.HTTPConnection(ip, port, timeout=1)
            sock.request("GET", "/falsealarm")
            print("[#] False alarm sended")
        except:
            http_client.connection_closed()

def get_state():
    connected = param_co.state_co["hubium"]["connected"]
    ip = param_co.state_co["hubium"]["ip"]
    port = param_co.state_co["hubium"]["http_server_port"]
    if(connected):
        try:
            sock = client.HTTPConnection(ip, port, timeout=1)
            sock.request("GET", "/state_hu")
            response = sock.getresponse()
            data = response.read()
            parser_json.upload_file_by_sock_data(param_co.path_state_hu, data)
            param_co.state_hu = parser_json.load_file(param_co.path_state_hu)
            sock.close()
        except:
            http_client.connection_closed()

def get_image():
    connected = param_co.state_co["hubium"]["connected"]
    ip = param_co.state_co["hubium"]["ip"]
    port = param_co.state_co["hubium"]["http_server_port"]
    if(connected):
        try:
            sock = client.HTTPConnection(ip, port, timeout=1)
            sock.request("GET", "/image")
            response = sock.getresponse()
            data_binary = response.read()

            # Save image
            img = open(param_co.path_image, "wb")
            img.write(data_binary)
            img.close()

            sock.close()
        except:
            http_client.connection_closed()
