#! /usr/bin/python
#---------------------------------------------

from param import param_co

from src import http
from src import http_get
from src import file

from gui import gui_update

from threading import Thread

import time


def start_thread_test_conn():
    param_co.run_thread_con = True
    thread_con = Thread(target = thread_test_connection)
    thread_con.start()

def thread_test_connection():
    while param_co.run_thread_con:
        # Test connections
        http.test_connection()
        http_get.get_state()
        gui_update.update_gui()

        # Update state
        file.update_state_file()
        file.upload_hu_state()

        # Wait for 1 second
        time.sleep(1)
        pass

def stop_thread():
    param_co.run_loop = False
    param_co.run_thread_con = False
