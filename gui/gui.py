#! /usr/bin/python
#---------------------------------------------

from param import cla

from src import loop

from scheme import scheme
from scheme import scheme_loop
from scheme import scheme_theme

from gui import gui_menu
from gui import gui_image

import dearpygui.dearpygui as dpg


def program():
    dpg.create_context()

    #Build GUI
    gui_image.init_image()
    with dpg.window(tag="window", label="Controlium"):
        gui_menu.menu()
        scheme.build_scheme()

    #Main GUI theme
    scheme_theme.global_theme()

    # Setup GUI
    dpg.create_viewport(title='Controlium', width=cla.contro.gui_width, height=cla.contro.gui_height)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("window", True)

    # Init variables
    loop.init()

    # Start main loop program
    while cla.contro.run_loop and dpg.is_dearpygui_running():
        loop.loop()
        scheme_loop.loop()
        dpg.render_dearpygui_frame()

    # End thread
    loop.end()

    # Finish program
    dpg.destroy_context()
