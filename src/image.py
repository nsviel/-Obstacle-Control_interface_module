#---------------------------------------------
from param import param_co
from scheme import scheme_update
from HTTPS import https_client_get
from src import terminal

import threading
import time


def start_daemon():
    param_co.run_thread_image = True
    thread_con = threading.Thread(target = thread_image)
    thread_con.start()
    terminal.addDaemon("#", "ON", "Image loader")

def stop_daemon():
    param_co.run_thread_image = False
    terminal.addDaemon("#", "OFF", "Image loader")

def thread_image():
    while param_co.run_thread_image:
        # Load current image
        ok = https_client_get.get_image("hu")

        # Update image
        if(ok):
            scheme_update.update_image()

        # Wait for 1 second
        time.sleep(0.1)
