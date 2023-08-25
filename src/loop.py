#---------------------------------------------
from src import daemon
from src.param import param_control
from src.gui import gui
from src.element import element
from src.state import state
from src.utils import saving
from src.utils import terminal
from src.utils import parser_json
from src.element.misc.wallet import wallet_logic

import time


def program():
    init()
    loop()
    end()

def init():
    state.load_configuration()
    saving.determine_path()
    element.object.init_objects()
    daemon.start_daemons()
    wallet_logic.initialization()
    gui.initialization()
    terminal.addLog("OK", "Program initialized...")
    terminal.addLine()

def loop():
    is_running = True
    param_control.run_loop = True
    while param_control.run_loop and is_running:
        is_running = gui.loop()

def end():
    terminal.shutdown()
    #gui.termination()
    parser_json.upload_state()
    daemon.stop_daemons()
    terminal.delai()
