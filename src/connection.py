#! /usr/bin/python
#---------------------------------------------

from param import param_co

from HTTP import http_client
from HTTP import http_client_get

from src import saving
from src import parser_json

from scheme import scheme_update

from threading import Thread

import threading
import socket
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
        saving.test_ssd_con()

        # Update state
        parser_json.upload_state()
        scheme_update.update()
        update_nb_thread()

        # Wait for 1 second
        time.sleep(1)
        pass

def connection_closed():
    param_co.state_co["hubium"]["http_connected"] = False
    param_co.state_co["hubium"]["sock_connected"] = False
    param_co.state_hu["sncf"]["connected"] = False
    param_co.state_hu["velodium"]["connected"] = False
    param_co.state_hu["pywardium"]["http_connected"] = False
    param_co.state_hu["pywardium"]["sock_connected"] = False

def get_ip_adress():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def update_nb_thread():
    param_co.state_co["self"]["nb_thread"] = threading.active_count()
