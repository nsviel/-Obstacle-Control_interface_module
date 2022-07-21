#! /usr/bin/python
#---------------------------------------------

from param import param_co
from src import data

from threading import Thread

import socket


def thread_socket_server():
    port = param_co.state_co["self"]["sock_server_port"]

    param_co.sock_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    param_co.sock_server.bind(("127.0.0.1", port))
    param_co.sock_server.settimeout(1)
    param_co.run_thread_socket = True

    while param_co.run_thread_socket:
        try:
            param_co.state_co["hubium"]["sock_connected"] = False
            data, (address, port) = param_co.sock_server.recvfrom(4096)
            param_co.state_co["hubium"]["sock_connected"] = True
            process_data(data)
        except:
            pass

    param_co.sock_server.close()

def process_data(data):
    msg = 0
    try:
        msg = data.decode('utf-8')
    except:
        pass
    if(msg == "ok"):
        param_hu.state_hu["velodium"]["connected"] = True
    else:
        data.process_lidar_1_data(data)
