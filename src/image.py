#! /usr/bin/python
#---------------------------------------------

from param import param_co
from scheme import scheme_update
from conn import http_client_get

from threading import Thread

import time


def start_daemon():
    param_co.run_thread_image = True
    thread_con = Thread(target = thread_image)
    thread_con.start()

def stop_daemon():
    param_co.run_thread_image = False

def thread_image():
    while param_co.run_thread_image:
        # Load current image
        http_client_get.get_image()

        # Update image
        scheme_update.update_image()

        # Wait for 1 second
        time.sleep(0.1)
        pass
