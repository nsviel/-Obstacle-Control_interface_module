#---------------------------------------------
from param import param_co
from src import data

from threading import Thread

import socket


def thread_socket_l1_server():
    port = param_co.state_co["self"]["sock_server_l1_port"]

    param_co.sock_server_l1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    param_co.sock_server_l1.bind(("", port))
    param_co.sock_server_l1.settimeout(1)
    param_co.run_thread_socket = True

    while param_co.run_thread_socket:
        try:
            data, (address, port) = param_co.sock_server_l1.recvfrom(4096)
            param_co.state_co["hubium"]["sock_l1_connected"] = True
            process_packet_l1(data)
        except:
            param_co.state_co["hubium"]["sock_l1_connected"] = False

    param_co.sock_server_l1.close()

def thread_socket_l2_server():
    port = param_co.state_co["self"]["sock_server_l2_port"]

    param_co.sock_server_l2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    param_co.sock_server_l2.bind(("", port))
    param_co.sock_server_l2.settimeout(1)
    param_co.run_thread_socket = True

    while param_co.run_thread_socket:
        try:
            data, (address, port) = param_co.sock_server_l2.recvfrom(4096)
            param_co.state_co["hubium"]["sock_l2_connected"] = True
            process_packet_l2(data)
        except:
            param_co.state_co["hubium"]["sock_l2_connected"] = False

    param_co.sock_server_l2.close()

def process_packet_l1(packet):
    msg = 0
    try:
        msg = packet.decode('utf-8')
    except:
        pass
    if(msg == "ok"):
        param_hu.state_hu["velodium"]["sock_connected"] = True
    else:
        data.process_l1_data(packet)

def process_packet_l2(packet):
    msg = 0
    try:
        msg = packet.decode('utf-8')
    except:
        pass
    if(msg == "ok"):
        param_hu.state_hu["velodium"]["sock_connected"] = True
    else:
        data.process_l2_data(packet)
