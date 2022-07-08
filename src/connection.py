#! /usr/bin/python
#---------------------------------------------

from param import param_co
from param import param_hu

from src import http
from src import http_get
from src import file

from gui import gui_update

from threading import Thread

import time


def start_thread_test_conn():
    param_co.run_thread_con = True
    thread_con = Thread(target = thread_test_connection)
    thread_con.start()

def thread_test_connection():
    while param_co.run_thread_con:
        # Test connections
        http.test_connection()
        http_get.get_state()
        gui_update.update_gui()

        # Update state
        file.update_state_file()
        file.upload_hu_state()

        # Wait for 1 second
        time.sleep(1)
        pass

def stop_thread():
    param_co.run_loop = False
    param_co.run_thread_con = False

def parse_state_json():
    param_hu.mqtt_connected = param_hu.hubium_json["mqtt"]["connected"]
    param_hu.velo_connected = param_hu.hubium_json["velodium"]["connected"]
    param_hu.vale_connected = param_hu.hubium_json["valeo"]["connected"]
    param_hu.edge_connected = param_hu.hubium_json["edge"]["connected"]
    param_hu.ai_connected = param_hu.hubium_json["ai"]["connected"]
