#! /usr/bin/python
#---------------------------------------------

from param import param_co
from HTTP import http_client_con
from src import parser_json

import http.client
import json
import time


def send_get_request(command, sucess):
    connected = param_co.state_co["hubium"]["http_connected"]
    ip = param_co.state_co["hubium"]["ip"]
    port = param_co.state_co["hubium"]["http_server_port"]
    if(connected):
        try:
            client = http.client.HTTPConnection(ip, port, timeout=1)
            client.request("GET", command)
        except:
            http_client_con.connection_hu_close()

def send_post_option(command, option, value):
    connected = param_co.state_co["hubium"]["http_connected"]
    ip = param_co.state_co["hubium"]["ip"]
    port = param_co.state_co["hubium"]["http_server_port"]

    header = {"Content-type": "application/json"}
    payload = {option: value}
    file = json.dumps(payload)

    if(connected):
        try:
            client = http.client.HTTPConnection(ip, port, timeout=1)
            client.request("POST", command, file, header)
            client.close()
        except:
            print("[\033[1;31merror\033[0m] Command \033[1;36m%s\033[0m to ip \033[1;36m%s\033[0m port \033[1;36m%d\033[0m failed" % (command, ip, port))

def send_post_request(command, lvl1, lvl2, value):
    connected = param_co.state_co["hubium"]["http_connected"]
    ip = param_co.state_co["hubium"]["ip"]
    port = param_co.state_co["hubium"]["http_server_port"]

    header = {"Content-type": "application/json"}
    payload = {lvl1: {lvl2: value}}
    file = json.dumps(payload)

    if(connected):
        try:
            client = http.client.HTTPConnection(ip, port, timeout=1)
            client.request("POST", command, file, header)
            client.close()
        except:
            print("[\033[1;31merror\033[0m] Command \033[1;36m%s\033[0m to ip \033[1;36m%s\033[0m port \033[1;36m%d\033[0m failed" % (command, ip, port))

def send_get_state(name):
    connected = param_co.state_co["hubium"]["http_connected"]
    ip = param_co.state_co["hubium"]["ip"]
    port = param_co.state_co["hubium"]["http_server_port"]
    if(connected):
        try:
            client = http.client.HTTPConnection(ip, port, timeout=1)
            client.request("GET", name)
            response = client.getresponse()
            state = response.read()
            client.close()
            return state
        except:
            pass

def send_get_image(path):
    connected = param_co.state_co["hubium"]["http_connected"]
    ip = param_co.state_co["hubium"]["ip"]
    port = param_co.state_co["hubium"]["http_server_port"]
    if(connected):
        try:
            client = http.client.HTTPConnection(ip, port, timeout=1)
            client.request("GET", "/image")
            response = client.getresponse()
            data_binary = response.read()

            # Save image
            if(len(data_binary) != 0):
                img = open(path, "wb")
                img.write(data_binary)
                img.close()

            client.close()
        except:
            http_client_con.connection_hu_close()
