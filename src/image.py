#! /usr/bin/python
#---------------------------------------------

from param import cla
from scheme import scheme_update
from src import http_client_get

from threading import Thread

import time


def start_thread_image():
    cla.contro.run_thread_image = True
    thread_con = Thread(target = thread_image)
    thread_con.start()

def thread_image():
    while cla.contro.run_thread_image:
        # Load current image
        http_client_get.get_image()

        # Update image
        scheme_update.update_image()

        # Wait for 1 second
        time.sleep(0.1)
        pass
