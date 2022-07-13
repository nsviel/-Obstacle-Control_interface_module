#! /usr/bin/python
#---------------------------------------------

from param import param_co

from src import http_client
from src import http_client_get
from src import file
from src import saving

from scheme import scheme_update

from threading import Thread

import time


def start_thread_test_conn():
    param_co.run_thread_con = True
    thread_con = Thread(target = thread_test_connection)
    thread_con.start()

def thread_test_connection():
    while param_co.run_thread_con:
        # Test connections
        http_client.test_connection()
        http_client_get.get_state_hu()
        http_client_get.get_state_py()
        saving.test_ssd_con()

        # Update state
        scheme_update.update()

        # Wait for 1 second
        time.sleep(1)
        pass

def stop_thread():
    param_co.run_loop = False
    param_co.run_thread_con = False
    param_co.run_thread_image = False
