#! /usr/bin/python
#---------------------------------------------

from param import param_co

from src import connection
from src import file


def init():
    file.init_state()
    connection.start_thread_test_conn()
    param_co.status = "Online"

def loop():
    a=1

def end():
    param_co.status = "Offline"
    file.update_state_file()
    connection.stop_thread()
