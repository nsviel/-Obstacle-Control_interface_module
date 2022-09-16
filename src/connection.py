#---------------------------------------------
from param import param_co

from HTTP import http_client_con
from HTTP import http_client_get
from HTTP import http_client_post

from src import saving
from src import parser_json
from src import signal

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
        http_client_con.test_hu_con()
        http_client_get.get_state_hu()
        http_client_get.get_state_py()
        saving.test_ssd_con()

        # Update state
        parser_json.upload_state()
        scheme_update.update_scheme()
        signal.update_nb_thread()
        update_status()

        # Wait for 1 second
        time.sleep(1)

def update_status():
    param_co.status_co = "Offline"
    param_co.status_hu = "Offline"
    param_co.status_py = "Offline"
    param_co.status_ve = "Offline"
    param_co.status_ai = "Offline"
    param_co.status_ed = "Offline"
    param_co.status_ssd = "Offline"
    param_co.status_sncf = "Offline"
    param_co.status_l1 = "Offline"
    param_co.status_l2 = "Offline"

    param_co.status_co = "Online"
    if(param_co.state_co["ssd"]["connected"]):
        param_co.status_ssd = "Online"
    if(param_co.state_co["hubium"]["http_connected"]):
        param_co.status_hu = "Online"
        if(param_co.state_hu["pywardium"]["http_connected"]):
            param_co.status_py = "Online"
            if(param_co.state_py["lidar_1"]["connected"]):
                param_co.status_l1 = "Online"
            if(param_co.state_py["lidar_2"]["connected"]):
                param_co.status_l2 = "Online"
        if(param_co.state_hu["ai"]["http_connected"]):
            param_co.status_ai = "Online"
        if(param_co.state_hu["velodium"]["http_connected"]):
            param_co.status_ve = "Online"
        if(param_co.state_hu["edge"]["http_connected"]):
            param_co.status_ed = "Online"
        if(param_co.state_hu["sncf"]["broker_connected"]):
            param_co.status_sncf = "Online"
