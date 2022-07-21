#! /usr/bin/python
#---------------------------------------------

from param import param_co


def get_ip_from_key(key):
    for i in range(0, len(param_co.wallet_add)):
        if(param_co.wallet_add[i] == key):
            return param_co.wallet_ip[i]
    return "None"
