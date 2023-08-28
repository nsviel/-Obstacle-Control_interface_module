#---------------------------------------------
# Possible POST command:
# - /trainope_param
# - /edge_state
# - /capture_state
# - /edge_param
# - /capture_param
# - /processing_param
# - /ai_param
#---------------------------------------------

from src.param import param_control
from src.connection.HTTPS import https_client_fct
from src.utils import terminal

import json
import http.client


def post_param_value(dest, lvl1, lvl2, value):
    [ip, port, connected] = https_client_fct.network_info(dest)
    command = "/" + dest + "_param"
    payload = json.dumps({lvl1: {lvl2: value}})
    https_client_fct.send_https_post(ip, port, connected, command, payload)
    terminal.addPost(dest, lvl1, lvl2, value)

def post_state(dest, state):
    [ip, port, connected] = https_client_fct.network_info(dest)
    command = "/state_" + dest
    payload = json.dumps(state).encode(encoding='utf_8')
    https_client_fct.send_https_post(ip, port, connected, command, payload)
    terminal.addLog("com", "To %s state"% dest)
