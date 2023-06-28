#!/usr/bin/env python3
#---------------------------------------------
from src.gui import gui
from src.utils import signal


signal.system_clear()
signal.manage_args()
signal.system_information("Control Interface")
#-------------

gui.program()

#-------------
print("-----------------------")
print("Program \033[1;34mexit\033[0m")
