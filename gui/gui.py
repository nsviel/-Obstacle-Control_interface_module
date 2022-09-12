#! /usr/bin/python
#---------------------------------------------

from param import param_co

from src import loop
from src import state
from src import wallet

from scheme import scheme
from scheme import scheme_loop
from scheme import scheme_theme
from scheme import scheme_update

from gui import gui_menu
from gui import gui_image
from gui import gui_wallet
from gui import gui_theme

import dearpygui.dearpygui as dpg


def program():
    dpg.create_context()

    #Initialization
    state.load_configuration()
    gui_image.init_image()
    wallet.read_wallet()
    wallet.determine_adresse()

    #Build GUI
    with dpg.window(label="Wallet", autosize=True, no_resize=True, show=False, tag="win_wallet"):
        gui_wallet.build_window()
    with dpg.window(tag="window", label="Controlium"):
        gui_menu.menu()
        scheme.build_scheme()

    #Main GUI theme
    gui_theme.gui_theme()
    scheme_theme.scheme_theme()

    # Setup GUI
    gui_width = param_co.state_co["gui"]["width"]
    gui_height = param_co.state_co["gui"]["height"]
    dpg.create_viewport(title='Controlium', width=gui_width, height=gui_height)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("window", True)
    scheme_update.update_add()

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
