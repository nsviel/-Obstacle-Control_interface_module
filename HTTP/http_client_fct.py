#! /usr/bin/python
#---------------------------------------------

from param import param_co

import http.client


def send_http_ping(ip, port):
    client = http.client.HTTPConnection(ip, port, timeout=0.1)
    connected = False
    try:
        client.request("GET", "/test_http_conn")
        connected = True
    except:
        connected = False
    client.close()
    return connected

def send_http_post(ip, port, connected, command, payload):
    if(connected):
        try:
            client = http.client.HTTPConnection(ip, port, timeout=1)
            header = {"Content-type": "application/json"}
            client.request("POST", command, payload, header)
            client.close()
        except:
            print("[\033[1;31merror\033[0m] Command \033[1;36m%s\033[0m to ip \033[1;36m%s\033[0m port \033[1;36m%d\033[0m failed" % (command, ip, port))

def send_http_get(ip, port, connected, command):
    data = None
    if(connected):
        try:
            client = http.client.HTTPConnection(ip, port, timeout=1)
            client.request("GET", command)
            response = client.getresponse()
            data = response.read()
            client.close()
        except:
            pass
    return data

def network_info(dest):
    ip = param_co.state_co["hubium"]["ip"]
    port = param_co.state_co["hubium"]["http_server_port"]
    connected = param_co.state_co["hubium"]["http_connected"]

    return [ip, port, connected]
