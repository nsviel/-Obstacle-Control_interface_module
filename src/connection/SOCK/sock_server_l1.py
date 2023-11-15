#---------------------------------------------
from src.param import param_control
from src.utils import terminal
from src.base import daemon
from src.element import element
import socket


class Socket_l1(daemon.Daemon):
    def __init__(self):
        self.socket = None

    def thread_init(self):
        port = param_control.state_control["control"]["socket"]["server_l1_port"]
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(("", port))
        self.socket.settimeout(1)

    def thread_function(self):
        try:
            packet, (address, port) = self.socket.recvfrom(4096)
            element.object.edge.data.plot.process_l1_data(packet)
            param_control.state_control["interface"]["edge"]["sock_l1_connected"] = True
        except:
            param_control.state_control["interface"]["edge"]["sock_l1_connected"] = False

    def thread_end(self):
        self.socket.close()

    name = "Socket server LiDAR 1";
    run_sleep = 0;
