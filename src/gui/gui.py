#---------------------------------------------
from src.param import param_co

from src import loop
from src.misc import state
from src.misc import wallet

from src.scheme import scheme
from src.scheme import scheme_theme
from src.scheme import scheme_update
from src.scheme import scheme_visibility
from src.scheme import scheme_link

from src.gui import gui_menu
from src.gui import gui_image
from src.gui import gui_wallet
from src.gui import gui_theme
from src.gui import gui_module

import dearpygui.dearpygui as dpg


def program():
    dpg.create_context()

    #Initialization
    state.load_configuration()
    gui_image.init_image()
    wallet.read_wallet()
    wallet.determine_adresse()
    gui_theme.gui_font()

    #Build GUI
    with dpg.window(label="Wallet", autosize=True, no_resize=True, show=False, tag="win_wallet"):
        gui_wallet.build_window()
    with dpg.window(tag="window", label="module_interface"):
        dpg.bind_font(param_co.gui_font_def)
        gui_menu.menu()
        scheme.build_scheme()
    scheme_theme.scheme_theme_dev()

    # Setup GUI
    gui_width = param_co.state_co["gui"]["width"]
    gui_height = param_co.state_co["gui"]["height"]
    dpg.create_viewport(title='module_interface', width=gui_width, height=gui_height)
    dpg.set_viewport_resizable(False)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("window", True)
    scheme_update.update_add()

    # Init variables
    loop.init()
    scheme_visibility.set_mode()

    # Start main loop program
    while param_co.run_loop and dpg.is_dearpygui_running():
        loop.loop()
        dpg.render_dearpygui_frame()

    # End thread
    loop.end()

    # Finish program
    dpg.destroy_context()
