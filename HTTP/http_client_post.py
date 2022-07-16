#! /usr/bin/python
#---------------------------------------------

from HTTP import http_client_fct


def post_param_py(lvl1, lvl2, value):
    http_client_fct.send_param_request("/new_param_py", lvl1, lvl2, value)

def post_param_hu(lvl1, lvl2, value):
    http_client_fct.send_param_request("/new_param_hu", lvl1, lvl2, value)
