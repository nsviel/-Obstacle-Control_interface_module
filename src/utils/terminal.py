#---------------------------------------------
# Terminal output functions
#---------------------------------------------
from src.param import param_control

import time


def addLog(type, message):
    if(type == "#"):
        print("[\033[1;34m#\033[0m]     "+ message)
    elif(type == "OK"):
        print("[\033[1;32mOK\033[0m]    "+ message)
    elif(type == "error"):
        print("[\033[1;31merror\033[0m] "+ message)
    elif(type == "com"):
        print("[\033[1;30mPOST\033[0m]  "+ message)
    time.sleep(param_control.tic_message)

def addPost(dest, c1, c2, c3):
    message = "To %s [%s, %s, %s]"%(dest, c1, c2, c3)

    print("[\033[1;30mPOST\033[0m]  " + message)
    time.sleep(param_control.tic_message)

def addDaemon(type, status, message):
    if(type == "#"):
        print("[\033[1;34m#\033[0m]     Daemon ", flush=True, end='')
    elif(type == "OK"):
        print("[\033[1;32mOK\033[0m]    Daemon ", flush=True, end='')
    elif(type == "error"):
        print("[\033[1;31merror\033[0m] Daemon ", flush=True, end='')

    if(status == "ON"):
        print("\033[1;32m"+status+"\033[0m - "+message)
    elif(status == "OFF"):
        print("\033[1;31m"+status+"\033[0m - "+message)

    time.sleep(param_control.tic_message)

def addLine():
    print("")

def shutdown():
    addLine()
    addLine()
    print("[\033[1;32mOK\033[0m]    Program shutdown ...",)

def delai():
    print("[\033[1;34m#\033[0m]     Daemon closing", flush=True, end='')
    print("...2", flush=True, end='')
    time.sleep(1)
    print("...1", flush=True)
    time.sleep(1)
