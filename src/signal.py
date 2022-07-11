#! /usr/bin/python
#---------------------------------------------

from param import classes

import signal
import time
import keyboard


# Manage Ctrl+C input
def handler(signum, frame):
    classes.contro.run_loop = False

signal.signal(signal.SIGINT, handler)

#Manage Esc keyboard button
def action_keyboard():
    try:
        if keyboard.is_pressed('esc'):
            classes.contro.run_loop = False
    except:
        a=1
