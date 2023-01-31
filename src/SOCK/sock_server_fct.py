#---------------------------------------------
from src.param import param_co
from src.misc import data
from src.misc import connection

import socket


def thread_socket_l1_server():
    port = param_co.state_co["self"]["sock_server_l1_port"]

    param_co.sock_server_l1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    param_co.sock_server_l1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    param_co.sock_server_l1.bind(("", port))
    param_co.sock_server_l1.settimeout(1)
    param_co.run_thread_socket = True

    while param_co.run_thread_socket:
        try:
            packet, (address, port) = param_co.sock_server_l1.recvfrom(4096)
            data.process_l1_data(packet)
            param_co.state_co["hubium"]["sock_l1_connected"] = True
        except:
            param_co.state_co["hubium"]["sock_l1_connected"] = False

    param_co.sock_server_l1.close()

def thread_socket_l2_server():
    port = param_co.state_co["self"]["sock_server_l2_port"]

    param_co.sock_server_l2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    param_co.sock_server_l2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    param_co.sock_server_l2.bind(("", port))
    param_co.sock_server_l2.settimeout(1)
    param_co.run_thread_socket = True

    # Socket loop
    while param_co.run_thread_socket:
        try:
            packet, (address, port) = param_co.sock_server_l2.recvfrom(4096)
            data.process_l2_data(packet)
            param_co.state_co["hubium"]["sock_l2_connected"] = True
        except:
            param_co.state_co["hubium"]["sock_l2_connected"] = False

    param_co.sock_server_l2.close()
