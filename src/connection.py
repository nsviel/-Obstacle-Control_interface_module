#! /usr/bin/python
#---------------------------------------------

from param import param_co

from HTTP import http_client
from HTTP import http_client_get
from HTTP import http_client_post

from src import saving
from src import parser_json
from src import status

from scheme import scheme_update

from threading import Thread

import time


def start_daemon():
    param_co.run_thread_con = True
    thread_con = Thread(target = thread_test_connection)
    thread_con.start()
    print("[\033[1;32mOK\033[0m] Start connection testing daemon")

def stop_daemon():
    param_co.run_thread_con = False

def thread_test_connection():
    while param_co.run_thread_con:
        # Test connections
        http_client.test_connection()
        http_client_get.get_state_hu()
        http_client_get.get_state_py()
        http_client_post.post_param_hu("controlium", "ip", param_co.state_co["self"]["ip"])
        saving.test_ssd_con()

        # Update state
        parser_json.upload_state()
        scheme_update.update()
        status.update_nb_thread()

        # Wait for 1 second
        time.sleep(1)

def connection_closed():
    param_co.state_co["hubium"]["http_connected"] = False
    param_co.state_co["hubium"]["sock_l1_connected"] = False
    param_co.state_co["hubium"]["sock_l2_connected"] = False
    param_co.state_hu["sncf"]["broker_connected"] = False
    param_co.state_hu["velodium"]["sock_connected"] = False
    param_co.state_hu["pywardium"]["http_connected"] = False
    param_co.state_hu["pywardium"]["sock_l1_connected"] = False
    param_co.state_hu["pywardium"]["sock_l2_connected"] = False
