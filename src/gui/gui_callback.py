#---------------------------------------------
from src.param import param_interface
from src.connection.HTTPS import https_client_post
from src.utils import wallet
from src.gui import gui_wallet
from src.scheme.loop import scheme_update
from src.scheme.style import scheme_mode_visibility

import dearpygui.dearpygui as dpg
import dearpygui.demo as demo


def callback_demo():
    demo.show_demo()

def callback_close():
    param_interface.run_loop = False

def callback_wallet_add():
    new_add = dpg.get_value("wallet_new_add")
    new_ip = dpg.get_value("wallet_new_ip")
    wallet.add_new_item(new_add, new_ip)
    dpg.set_value("wallet_new_add", "")
    dpg.set_value("wallet_new_ip", "")
    gui_wallet.destroy_table()
    gui_wallet.build_table()
    scheme_update.update_add_combo()

def callback_wallet_remove(sender):
    wallet.remoprocessing_item_id(sender)
    gui_wallet.destroy_table()
    gui_wallet.build_table()
    scheme_update.update_add_combo()

def callback_mode_dev():
    param_interface.status_ui = "param"
    scheme_mode_visibility.set_mode()

def callback_mode_demo_minimized():
    dpg.hide_item("node_py")
    dpg.hide_item("node_edge_1")
    dpg.hide_item("node_data")
    dpg.hide_item("node_operator")
    dpg.hide_item("node_train")
    dpg.render_dearpygui_frame()
    param_interface.status_ui = "overview"
    scheme_mode_visibility.set_mode()

def callback_mode_demo_fullscreen():
    param_interface.status_ui = "overview_fullscreen"
    scheme_mode_visibility.set_mode()

def callback_with_iperf():
    with_iperf = dpg.get_value("iperf_activated")
    https_client_post.post_param_value("capture", "network", "iperf_activated", with_iperf)
    https_client_post.post_param_value("edge", "network", "iperf_activated", with_iperf)
