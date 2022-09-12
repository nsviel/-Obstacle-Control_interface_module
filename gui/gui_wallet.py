#! /usr/bin/python
#---------------------------------------------

from param import param_co

from gui import gui_callback

import dearpygui.dearpygui as dpg


def build_window():
    with dpg.group(horizontal=True):
        dpg.add_text("Add:")
        dpg.add_input_text(tag="wallet_new_add", label="", width=200)
    with dpg.group(horizontal=True):
        dpg.add_text("IP: ")
        dpg.add_input_text(tag="wallet_new_ip", label="", width=200)
    dpg.add_button(label="Add item", callback=gui_callback.callback_wallet_add)
    dpg.add_separator()
    build_table()

def destroy_table():
    dpg.delete_item("wallet_table")

def build_table():
    with dpg.table(header_row=True, borders_innerH=True, tag="wallet_table", parent="win_wallet"):
        dpg.add_table_column(label="Address")
        dpg.add_table_column(label="IP")
        dpg.add_table_column(label="", width_fixed=True, init_width_or_weight=20)
        for i in range(len(param_co.wallet_add)):
            with dpg.table_row():
                dpg.add_text(param_co.wallet_add[i])
                dpg.add_text(param_co.wallet_ip[i])
                if(i > 5):
                    dpg.add_button(label="X", tag=str(i), callback=gui_callback.callback_wallet_remove)
