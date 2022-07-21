#! /usr/bin/python
#---------------------------------------------

from param import param_co
from SOCK import sock_server_fct

from threading import Thread


def start_daemon():
    thread_con = Thread(target = sock_server_fct.thread_socket_server)
    thread_con.start()
    print("[\033[1;32mOK\033[0m] Start socket server daemon")

def stop_daemon():
    param_co.run_thread_socket = False
