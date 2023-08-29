#---------------------------------------------
# Possible POST command:
# - /post_state_xxx
# - /post_command_xxx
#---------------------------------------------

from src.param import param_control
from src.connection.HTTPS.client import https_client_fct
from src.utils import terminal

import json
import http.client


def post_commande(dest, component, value):
    [ip, port, connected] = https_client_fct.network_info(dest)
    command = "/post_command_" + dest
    payload = json.dumps({component: value})
    https_client_fct.send_https_post(ip, port, connected, command, payload)
    terminal.addPost(dest, component, value)

def post_state(dest, state):
    [ip, port, connected] = https_client_fct.network_info(dest)
    command = "/post_state_" + dest
    payload = json.dumps(state).encode(encoding='utf_8')
    https_client_fct.send_https_post(ip, port, connected, command, payload)
