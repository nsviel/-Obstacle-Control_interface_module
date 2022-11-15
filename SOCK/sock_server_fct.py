#---------------------------------------------
from param import param_co
from src import data

import socket


def thread_socket_l1_server():
    port = param_co.state_co["self"]["sock_server_l1_port"]

    param_co.sock_server_l1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    param_co.sock_server_l1.bind(("", port))
    param_co.sock_server_l1.settimeout(1)
    param_co.run_thread_socket = True

    while param_co.run_thread_socket:
        try:

            packet, (address, port) = param_co.sock_server_l1.recvfrom(4096)
            print("l1")
            data.process_l1_data(packet)
            param_co.state_co["hubium"]["sock_l1_connected"] = True
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
            print("nop")
            print(port)
            packet = param_co.sock_server_l2.recvfrom(4096)
            print("l2")
            data.process_l2_data(packet)
            print("2")
            param_co.state_co["hubium"]["sock_l2_connected"] = True
        except:
            param_co.state_co["hubium"]["sock_l2_connected"] = False

    param_co.sock_server_l2.close()
