#! /usr/bin/python
#---------------------------------------------

from param import param_co

from threading import Thread

import socket


def thread_socket_server():
    port = param_co.state_co["self"]["sock_server_port"]
    ip = param_co.state_co["pywardium"]["ip"]

    param_co.sock_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    param_co.sock_server.bind(("127.0.0.1", port))
    param_co.sock_server.settimeout(1)
    param_co.run_thread_socket = True

    while param_co.run_thread_socket:
        try:
            param_co.state_co["pywardium"]["sock_connected"] = False
            data, (address, port) = param_co.sock_server.recvfrom(4096)
            param_co.state_co["pywardium"]["sock_connected"] = True
            process_data(data)
        except:
            pass

    param_co.sock_server.close()

def process_data():
    msg = data.decode('utf-8')
    if(msg == "ok"):
        param_co.state_hu["velodium"]["connected"] = True
