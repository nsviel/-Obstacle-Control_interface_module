#---------------------------------------------
from src.param import param_interface

from src.HTTPS import https_client_con
from src.HTTPS import https_client_get
from src.HTTPS import https_client_post

from src.misc import saving
from src.misc import parser_json
from src.misc import signal
from src.misc import state
from src.misc import terminal

from src.scheme import scheme_loop
from src.scheme import scheme_update

import threading
import time
import socket


def start_daemon():
    param_interface.run_thread_con = True
    thread_con = threading.Thread(target = thread_test_connection)
    thread_con.start()
    terminal.addDaemon("#", "ON", "Connection tests")

def stop_daemon():
    param_interface.run_thread_con = False
    terminal.addDaemon("#", "OFF", "Connection tests")

def thread_test_connection():
    while param_interface.run_thread_con:
        # Test connections
        https_client_con.test_edge_con()
        saving.test_ssd_con()

        # Update state
        https_client_get.get_state("edge")
        https_client_get.get_state("acquisition")
        https_client_get.get_state("network")
        state.update_state()
        parser_json.upload_state()

        # Update scheme
        signal.update_nb_thread()
        scheme_update.update_scheme()
        scheme_loop.loop()

        # Wait for 1 second
        time.sleep(param_interface.tic_connection)

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
