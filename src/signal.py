#! /usr/bin/python
#---------------------------------------------

from param import cla

import signal
import time
import keyboard


# Manage Ctrl+C input
def handler(signum, frame):
    cla.contro.run_loop = False

signal.signal(signal.SIGINT, handler)

#Manage Esc keyboard button
def action_keyboard():
    try:
        if keyboard.is_pressed('esc'):
            cla.contro.run_loop = False
    except:
        a=1
