#! /usr/bin/python
#---------------------------------------------

from param import param_co

#from src import loop

#from gui import gui_loop
from gui import gui_build

import dearpygui.dearpygui as dpg


def program():
    dpg.create_context()

    #Build GUI
    with dpg.window(tag="window", label="Controlium"):
        gui_build.build()

    #Main GUI theme
    gui_build.build_theme()

    # Setup GUI
    dpg.create_viewport(title='Controlium', width=param_co.gui_width, height=param_co.gui_height)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("window", True)

    # Init variables
    #loop.init()

    # Start main loop program
    while param_co.run_loop and dpg.is_dearpygui_running():
        #loop.loop()
        #gui_loop.loop()
        dpg.render_dearpygui_frame()

    # End thread
    #loop.end()

    # Finish program
    dpg.destroy_context()
