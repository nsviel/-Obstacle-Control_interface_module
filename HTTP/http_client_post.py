#! /usr/bin/python
#---------------------------------------------
# Possible POST command:
# - /sncf_param
# - /hu_state
# - /py_state
# - /hu_param
# - /py_param
# - /ve_param
# - /ai_param
#---------------------------------------------

from param import param_co
from HTTP import http_client_fct

import json
import http.client


def post_param_payload(dest, payload):
    [ip, port, connected] = http_client_fct.network_info(dest)
    command = "/" + dest + "_param"
    http_client_fct.send_http_post(ip, port, connected, command, payload)

def post_param_value(dest, lvl1, lvl2, value):
    [ip, port, connected] = http_client_fct.network_info(dest)
    command = "/" + dest + "_param"
    payload = json.dumps({lvl1: {lvl2: value}})
    http_client_fct.send_http_post(ip, port, connected, command, payload)

def post_state(dest, state):
    [ip, port, connected] = http_client_fct.network_info(dest)
    command = "/" + dest + "_state"
    payload = json.dumps(state).encode(encoding='utf_8')
    http_client_fct.send_http_post(ip, port, connected, command, payload)
