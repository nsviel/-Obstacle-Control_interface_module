#---------------------------------------------
from param import param_co

from HTTPS import https_client_con
from HTTPS import https_client_get
from HTTPS import https_client_post

from src import saving
from src import parser_json
from src import signal
from src import state

from scheme import scheme_loop
from scheme import scheme_update

import threading
import time


def start_daemon():
    param_co.run_thread_con = True
    thread_con = threading.Thread(target = thread_test_connection)
    thread_con.start()
    print("[\033[1;32mOK\033[0m] Start connection testing daemon")

def stop_daemon():
    param_co.run_thread_con = False

def thread_test_connection():
    while param_co.run_thread_con:
        # Test connections
        https_client_con.test_hu_con()
        saving.test_ssd_con()

        # Update state
        https_client_get.get_state("hu")
        https_client_get.get_state("py")
        https_client_get.get_state("perf")
        state.update_state()
        parser_json.upload_state()

        # Update scheme
        signal.update_nb_thread()
        scheme_update.update_scheme()
        scheme_loop.loop()

        # Wait for 1 second
        time.sleep(1)
