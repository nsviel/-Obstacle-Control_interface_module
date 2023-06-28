#---------------------------------------------
from src.param import param_interface
from src.connection.SOCK import sock_server
from src.connection.DHCP import dhcp_client

from src.connection import connection
from src.utils import signal
from src.utils import saving
from src.scheme.node.data import image
from src.utils import parser_json
from src.state import state
from src.utils import wallet
from src.utils import terminal

import time

import os
def init():
    saving.determine_path()
    connection.start_daemon()
    sock_server.start_daemon()
    image.start_daemon()
    terminal.addLog("OK", "Program initialized...")
    terminal.addLine()

def loop():
    time.sleep(param_interface.tic_loop)

def end():
    terminal.shutdown()
    parser_json.upload_state()
    connection.stop_daemon()
    sock_server.stop_daemon()
    image.stop_daemon()
    terminal.delai()
