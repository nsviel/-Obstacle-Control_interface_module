#! /usr/bin/python
#---------------------------------------------

from param import param_co
from HTTP import http_client_fct
from src import parser_json

import json
import http.client


def post_param(command, cat, option, value):
    if(command != "/param_py" or command != "/param_ve" \
    or command != "/param_hu" or command != "/param_ai"):
        print("[error] http command wrong")
    http_client_fct.send_post_request(command, cat, option, value)

def post_param_py(cat, option, value):
    http_client_fct.send_post_request("/new_param_py", cat, option, value)

def post_param_hu(cat, option, value):
    http_client_fct.send_post_request("/new_param_hu", cat, option, value)

def post_param_ve(option, value):
    http_client_fct.send_post_option("/new_param_ve", option, value)

def post_param_ai(option, value):
    http_client_fct.send_post_option("/new_param_ai", option, value)

def send_hu_state():
    # Parameters
    ip = param_co.state_co["hubium"]["ip"]
    port = param_co.state_co["hubium"]["http_server_port"]
    connected = param_co.state_co["hubium"]["http_connected"]

    # Header
    header = {"Content-type": "application/json"}
    data = json.dumps(param_co.state_hu).encode(encoding='utf_8')
    command = "/new_state_hu"

    if(connected):
        try:
            client = http.client.HTTPConnection(ip, port, timeout=1)
            client.request("POST", command, data, header)
            client.close()
        except:
            print("[\033[1;31merror\033[0m] Command \033[1;36m%s\033[0m to ip \033[1;36m%s\033[0m port \033[1;36m%d\033[0m failed" % (command, ip, port))

def send_py_state():
    # Parameters
    ip = param_co.state_co["hubium"]["ip"]
    port = param_co.state_co["hubium"]["http_server_port"]
    connected = param_co.state_co["hubium"]["http_connected"]

    # Header
    header = {"Content-type": "application/json"}
    data = json.dumps(param_co.state_py).encode(encoding='utf_8')
    command = "/new_state_py"

    if(connected):
        try:
            client = http.client.HTTPConnection(ip, port, timeout=1)
            client.request("POST", command, data, header)
            client.close()
        except:
            print("[\033[1;31merror\033[0m] Command \033[1;36m%s\033[0m to ip \033[1;36m%s\033[0m port \033[1;36m%d\033[0m failed" % (command, ip, port))
