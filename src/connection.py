#! /usr/bin/python
#---------------------------------------------

from param import param_co

from HTTP import http_client_con
from HTTP import http_client_get
from HTTP import http_client_post

from src import saving
from src import parser_json
from src import status

from scheme import scheme_update

from threading import Thread

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
        http_client_con.test_hu_con()
        http_client_get.get_state("hu")
        http_client_get.get_state("py")
        saving.test_ssd_con()

        # Update state
        parser_json.upload_state()
        scheme_update.update()
        status.update_nb_thread()

        # Wait for 1 second
        time.sleep(1)

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
