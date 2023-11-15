#---------------------------------------------
from src.param import param_control
from src.utils import terminal

import socket
import threading
import platform
import signal
import time
import os
import getpass
import sys
import argparse
import psutil


# Manage Ctrl+C input
def handler(signum, frame):
    param_control.run_loop = False

signal.signal(signal.SIGINT, handler)

def system_clear():
    os.system('clear')

def update_nb_thread():
    param_control.state_control["control"]["info"]["nb_thread"] = threading.active_count()

def check_for_root():
    if not os.geteuid() == 0:
        sys.exit("\nOnly root can run this script\n")

def system_information(prog_name):
    check_for_root()

    # Retrieve program info
    program = prog_name
    ip = get_ip_adress()
    hostname = socket.gethostname()
    arch = platform.architecture()[0]
    core = platform.uname()[2]
    proc = platform.processor()
    python = platform.python_version()
    OS = get_OS()

    # Program header
    print('%-12s' '\033[1;34m%s\033[0m' % ("[Obstacle]", program))
    print("-----------------------")
    print('%-12s' '\033[1;34m%s\033[0m' % ("IP", ip))
    print('%-12s' '\033[1;34m%s\033[0m' % ("Hostname", hostname))
    print('%-12s' '\033[1;34m%s\033[0m, \033[1;34m%s\033[0m' % ("Arch", arch, proc))
    print('%-12s' '\033[1;34m%s\033[0m' % ("OS", OS))
    print('%-12s' '\033[1;34m%s\033[0m' % ("Core", core))
    print('%-12s' '\033[1;34m%s\033[0m' % ("Python", python))
    print("-----------------------")

def get_OS():
    try:
        OS = platform.freedesktop_os_release()['PRETTY_NAME']
    except:
        OS = platform.system()
    return OS

def get_temps_core(number):
    temp = psutil.sensors_temperatures()
    if(temp):
        try:
            temperature = temp["coretemp"][number+1].current
        except:
            temperature = 0
        return temperature

def get_ip_adress():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def get_username():
    try:
        user = os.getlogin()
    except:
        user = "."
