#! /usr/bin/python
#---------------------------------------------

from param import param_co

import signal
import time
import keyboard


# Manage Ctrl+C input
def handler(signum, frame):
    param_co.run_loop = False

signal.signal(signal.SIGINT, handler)

#Manage Esc keyboard button
def action_keyboard():
    try:
        if keyboard.is_pressed('esc'):
            param_co.run_loop = False
    except:
        a=1
