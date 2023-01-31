#---------------------------------------------
from src.param import param_co
from src.SOCK import sock_server_fct
from src.misc import terminal

import threading
import time


def start_daemon():
    thread_l1 = threading.Thread(target = sock_server_fct.thread_socket_l1_server)
    thread_l2 = threading.Thread(target = sock_server_fct.thread_socket_l2_server)
    thread_l1.start()
    thread_l2.start()
    terminal.addDaemon("#", "ON", "Socket server")

def stop_daemon():
    param_co.run_thread_socket = False
    terminal.addDaemon("#", "OFF", "Socket server")

def restart_daemon():
    terminal.addDaemon("#", "restart", "Socket server")
    stop_daemon()
    time.sleep(1)
    start_daemon()
