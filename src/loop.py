#! /usr/bin/python
#---------------------------------------------

from param import param_co

from src import connection
from src import file
from src import signal
from src import saving
from src import image


def init():
    file.load_configuration()
    saving.determine_path()
    connection.start_thread_test_conn()
    image.start_thread_image()
    param_co.state_co["self"]["status"] = "Online"

def loop():
    a=1
    #signal.action_keyboard()

def end():
    param_co.state_co["self"]["status"] = "Offline"
    parser_json.upload_file(param_co.path_state_co, param_co.state_co)
    connection.stop_thread()
