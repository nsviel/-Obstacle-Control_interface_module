#! /usr/bin/python
#---------------------------------------------

from param import param_co

from src import connection
from src import file
from src import signal


def init():
    file.init_state()
    connection.start_thread_test_conn()
    param_co.status = "Online"

def loop():
    a=1
    #signal.action_keyboard()

def end():
    param_co.status = "Offline"
    file.update_state_file()
    connection.stop_thread()
