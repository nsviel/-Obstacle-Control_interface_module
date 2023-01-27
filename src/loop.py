#---------------------------------------------
from param import param_co
from SOCK import sock_server
from DHCP import dhcp_client

from src import connection
from src import signal
from src import saving
from src import image
from src import parser_json
from src import state
from src import wallet
from src import terminal

import time


def init():
    saving.determine_path()
    connection.start_daemon()
    sock_server.start_daemon()
    image.start_daemon()
    terminal.addLog("OK", "Program initialized...")
    terminal.addLine()

def loop():
    time.sleep(0.033)

def end():
    terminal.shutdown()
    parser_json.upload_state()
    connection.stop_daemon()
    sock_server.stop_daemon()
    image.stop_daemon()
