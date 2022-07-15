#! /usr/bin/python
#---------------------------------------------

from param import param_co

from conn import http_client
from conn import http_client_get

from src import file
from src import saving
from src import parser_json

from scheme import scheme_update

from threading import Thread

import time


def start_daemon():
    param_co.run_thread_con = True
    thread_con = Thread(target = thread_test_connection)
    thread_con.start()

def stop_daemon():
    param_co.run_thread_con = False

def thread_test_connection():
    while param_co.run_thread_con:
        # Test connections
        http_client.test_connection()
        http_client_get.get_state_hu()
        http_client_get.get_state_py()
        saving.test_ssd_con()

        # Update state
        parser_json.upload_state()
        scheme_update.update()

        # Wait for 1 second
        time.sleep(1)
        pass

def connection_closed():
    param_co.state_co["hubium"]["connected"] = False
    param_co.state_py["self"]["sock_connected"] = False
    param_co.state_hu["sncf"]["connected"] = False
