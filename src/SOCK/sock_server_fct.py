#---------------------------------------------
from src.param import param_interface
from src.misc import data
from src.misc import connection

import socket


def thread_socket_l1_server():
    port = param_interface.state_interface["self"]["sock_server_l1_port"]

    param_interface.sock_server_l1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    param_interface.sock_server_l1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    param_interface.sock_server_l1.bind(("", port))
    param_interface.sock_server_l1.settimeout(1)
    param_interface.run_thread_socket = True

    while param_interface.run_thread_socket:
        try:
            packet, (address, port) = param_interface.sock_server_l1.recvfrom(4096)
            data.process_l1_data(packet)
            param_interface.state_interface["edge"]["sock_l1_connected"] = True
        except:
            param_interface.state_interface["edge"]["sock_l1_connected"] = False

    param_interface.sock_server_l1.close()

def thread_socket_l2_server():
    port = param_interface.state_interface["self"]["sock_server_l2_port"]

    param_interface.sock_server_l2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    param_interface.sock_server_l2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    param_interface.sock_server_l2.bind(("", port))
    param_interface.sock_server_l2.settimeout(1)
    param_interface.run_thread_socket = True

    # Socket loop
    while param_interface.run_thread_socket:
        try:
            packet, (address, port) = param_interface.sock_server_l2.recvfrom(4096)
            data.process_l2_data(packet)
            param_interface.state_interface["edge"]["sock_l2_connected"] = True
        except:
            param_interface.state_interface["edge"]["sock_l2_connected"] = False

    param_interface.sock_server_l2.close()
