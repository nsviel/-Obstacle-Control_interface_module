#---------------------------------------------
from param import param_co
from scheme import scheme_update
from HTTPS import https_client_get

import threading
import time


def start_daemon():
    param_co.run_thread_image = True
    thread_con = threading.Thread(target = thread_image)
    thread_con.start()
    print("[\033[1;32mOK\033[0m] Start image request daemon")

def stop_daemon():
    param_co.run_thread_image = False

def thread_image():
    while param_co.run_thread_image:
        # Load current image
        https_client_get.get_image("hu")

        # Update image
        scheme_update.update_image()

        # Wait for 1 second
        time.sleep(0.1)
