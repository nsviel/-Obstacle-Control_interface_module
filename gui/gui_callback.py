#! /usr/bin/python
#---------------------------------------------

from param import param_co
from HTTP import http_client_get
from src import wallet
from gui import gui_wallet
from scheme import scheme_update

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
