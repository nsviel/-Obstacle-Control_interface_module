#---------------------------------------------
from src.connection.HTTPS.client import https_client_con
from src.connection.HTTPS.client import https_client_get
from src.connection.HTTPS.client import https_client_post

from src.param import param_control
from src.element import element
from src.base import daemon
from src.state import state
from src.utils import saving
from src.utils import signal
from src.utils import terminal
from src.state import state

import socket


class Connection(daemon.Daemon):
    def __init__(self):
        self.name = "Connection";
        self.run_sleep = 0.5;
    def thread_function(self):
        # Test connections
        https_client_con.test_connection_edge()
        saving.test_ssd_con()

        # Update state
        https_client_get.get_state("edge")
        https_client_get.get_state("ground")
        https_client_get.get_state("network")
        https_client_get.get_state("cloud")
        state.upload_state()

        # Update scheme
        signal.update_nb_thread()

def check_port_open(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port))
    is_open = False
    if result == 0:
       is_open = True
    else:
        print("[\033[1;31merror\033[0m] Port \033[1;32m%d\033[0m is closed"% port)
    sock.close()
    return is_open;
