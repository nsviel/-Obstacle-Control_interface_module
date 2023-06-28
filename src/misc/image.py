#---------------------------------------------
from src.param import param_interface
from src.scheme.loop import scheme_update
from src.connection.HTTPS import https_client_get
from src.misc import terminal

import threading
import time


def start_daemon():
    param_interface.run_thread_image = True
    thread_con = threading.Thread(target = thread_image)
    thread_con.start()
    terminal.addDaemon("#", "ON", "Image loader")

def stop_daemon():
    param_interface.run_thread_image = False
    terminal.addDaemon("#", "OFF", "Image loader")

def thread_image():
    while param_interface.run_thread_image:
        # Load current image
        ok = https_client_get.get_image("edge")

        # Update image
        if(ok):
            scheme_update.update_image()

        # Wait for 1 second
        time.sleep(param_interface.tic_image)
