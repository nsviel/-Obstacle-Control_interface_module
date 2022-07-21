#! /usr/bin/python
#---------------------------------------------

from param import param_co

from src import loop
from src import state
from src import saving

from scheme import scheme
from scheme import scheme_loop
from scheme import scheme_theme
from scheme import scheme_update

from gui import gui_menu
from gui import gui_image

import dearpygui.dearpygui as dpg


def program():
    dpg.create_context()

    #Initialization
    state.load_configuration()
    gui_image.init_image()
    saving.read_wallet()

    #Build GUI
    with dpg.window(tag="window", label="Controlium"):
        gui_menu.menu()
        scheme.build_scheme()

    #Main GUI theme
    scheme_theme.global_theme()

    # Setup GUI
    gui_width = param_co.state_co["gui"]["width"]
    gui_height = param_co.state_co["gui"]["height"]
    dpg.create_viewport(title='Controlium', width=gui_width, height=gui_height)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("window", True)

    # Init variables
    loop.init()

    # Start main loop program
    while param_co.run_loop and dpg.is_dearpygui_running():
        loop.loop()
        scheme_loop.loop()
        dpg.render_dearpygui_frame()

    # End thread
    loop.end()

    # Finish program
    dpg.destroy_context()
