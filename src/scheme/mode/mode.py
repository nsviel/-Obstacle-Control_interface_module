#---------------------------------------------
from src.param import param_interface
from src.connection.HTTPS import https_client_get
from src.connection.HTTPS import https_client_post
from src.scheme.loop import scheme_update
from src.scheme.mode import mode_position
from src.scheme.mode import visibility_dev
from src.scheme.mode import visibility_demo

import dearpygui.dearpygui as dpg


def set_mode():
    if(param_interface.status_ui == "param"):
        visibility_dev.set_visibility()
        mode_position.update_node_pos_dev()
    elif(param_interface.status_ui == "overview"):
        visibility_demo.set_visibility()
        mode_position.update_node_pos_demo_minimized()
    elif(param_interface.status_ui == "overview_fullscreen"):
        visibility_demo.set_visibility()
        mode_position.update_node_pos_demo_fullscreen()
