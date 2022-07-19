#! /usr/bin/python
#---------------------------------------------

from param import param_co
from SOCK import sock_sever_fct

import threading


def start_daemon():
    thread_con = Thread(target = sock_sever_fct.thread_socket_server)
    thread_con.start()

def stop_daemon():
    param_co.run_thread_socket = False
