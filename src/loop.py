#---------------------------------------------
from src.param import param_interface
from src.SOCK import sock_server
from src.DHCP import dhcp_client

from src.misc import connection
from src.misc import signal
from src.misc import saving
from src.misc import image
from src.misc import parser_json
from src.misc import state
from src.misc import wallet
from src.misc import terminal

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
