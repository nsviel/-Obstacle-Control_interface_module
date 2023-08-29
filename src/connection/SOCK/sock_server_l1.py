#---------------------------------------------
from src.param import param_control
from src.utils import terminal
from src.base import daemon

import socket


class Socket_l1(daemon.Daemon):
    def thread_init(self):
        port = param_control.state_control["control"]["socket"]["server_l1_port"]
        param_control.sock_server_l1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        param_control.sock_server_l1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        param_control.sock_server_l1.bind(("", port))
        param_control.sock_server_l1.settimeout(1)

    def thread_function(self):
        try:
            packet, (address, port) = param_control.sock_server_l1.recvfrom(4096)
            data.process_l1_data(packet)
            param_control.state_control["control"]["interface"]["edge_sock_l1_connected"] = True
        except:
            param_control.state_control["control"]["interface"]["edge_sock_l1_connected"] = False

    def thread_end(self):
        param_control.sock_server_l1.close()

    name = "Socket server LiDAR 1";
    run_sleep = 0;
