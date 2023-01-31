#---------------------------------------------
from src.param import param_co
from src.HTTPS import https_client_post
from src.misc import wallet
from src.gui import gui_wallet
from src.scheme import scheme_update
from src.scheme import scheme_visibility

import dearpygui.dearpygui as dpg
import dearpygui.demo as demo


def callback_demo():
    demo.show_demo()

def callback_close():
    param_co.run_loop = False

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
    wallet.remove_item_id(sender)
    gui_wallet.destroy_table()
    gui_wallet.build_table()
    scheme_update.update_add_combo()

def callback_mode_dev():
    param_co.status_ui = "dev"
    scheme_visibility.set_mode()

def callback_mode_demo_minimized():
    dpg.hide_item("node_py")
    dpg.hide_item("node_hu")
    dpg.hide_item("node_data")
    dpg.hide_item("node_sncf")
    dpg.hide_item("node_train")
    dpg.render_dearpygui_frame()
    param_co.status_ui = "demo_minimized"
    scheme_visibility.set_mode()

def callback_mode_demo_fullscreen():
    param_co.status_ui = "demo_fullscreen"
    scheme_visibility.set_mode()

def callback_with_iperf():
    with_iperf = dpg.get_value("iperf_activated")
    https_client_post.post_param_value("py", "perf", "iperf_activated", with_iperf)
    https_client_post.post_param_value("hu", "perf", "iperf_activated", with_iperf)
