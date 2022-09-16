#---------------------------------------------
from param import param_co
from src import network

import socket
import threading
import platform
import signal
import time
import os
import getpass
import sys


# Manage Ctrl+C input
def handler(signum, frame):
    param_co.run_loop = False

signal.signal(signal.SIGINT, handler)

def system_clear():
    os.system('clear')

def update_nb_thread():
    param_co.state_co["self"]["nb_thread"] = threading.active_count()

def check_for_root():
    if not os.geteuid() == 0:
        sys.exit("\nOnly root can run this script\n")

def system_information(prog_name):
    check_for_root()

    #Info
    program = prog_name
    ip = network.get_ip_adress()
    hostname = socket.gethostname()
    arch = platform.architecture()[0]
    core = platform.uname()[2]
    proc = platform.processor()
    python = platform.python_version()

    try:
        OS = platform.freedesktop_os_release()['PRETTY_NAME']
    except:
        OS = platform.system()

    #Header
    print("Program \033[1;34m%s\033[0m"% program)
    print("-----------------------")
    print("IP \033[1;34m%s\033[0m"% ip)
    print("Hostname \033[1;34m%s\033[0m"% hostname)
    print("Arch \033[1;34m%s\033[0m, \033[1;34m%s\033[0m"% (arch, proc))
    print("OS \033[1;34m%s\033[0m"% OS)
    print("Core \033[1;34m%s\033[0m"% core)
    print("Python \033[1;34m%s\033[0m"% python)
    print("-----------------------")
