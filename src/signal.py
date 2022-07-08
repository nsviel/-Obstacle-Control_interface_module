#! /usr/bin/python
#---------------------------------------------

from param import param_co

import signal
import time


# Manage Ctrl+C input
def handler(signum, frame):
    param_co.run_loop = False

signal.signal(signal.SIGINT, handler)
