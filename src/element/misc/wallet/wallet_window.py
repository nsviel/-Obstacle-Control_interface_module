#---------------------------------------------
from src.param import param_control
from src.element.misc.wallet import wallet_logic
from src.element.misc.wallet import wallet_window
from src.gui.style import gui_color
from src.element.base import window
import dearpygui.dearpygui as dpg
import json


class Wallet_window(window.Window):
    def build_parameter(self):
        with dpg.group(horizontal=True):
            dpg.add_text("Add:")
            dpg.add_input_text(tag=self.ID.ID_new_address, label="", width=200)
        with dpg.group(horizontal=True):
            dpg.add_text("IP: ")
            dpg.add_input_text(tag=self.ID.ID_new_ip, label="", width=200)
        dpg.add_button(label="Add item", callback=self.callback_wallet_add())
        dpg.add_separator()
        with dpg.table(tag=self.ID.ID_table, header_row=True, borders_innerH=True, parent=self.ID.ID_window, policy=dpg.mvTable_SizingFixedFit):
            dpg.add_table_column(label="Address")
            dpg.add_table_column(label="IP")
            dpg.add_table_column(label="", width_fixed=True, init_width_or_weight=20)
            for i in range(len(param_control.wallet_add)):
                with dpg.table_row():
                    dpg.add_text(param_control.wallet_add[i])
                    dpg.add_text(param_control.wallet_ip[i])
                    if(i > 5):
                        dpg.add_button(label="X", tag=str(i), callback=self.callback_wallet_remove())

    # Subfunction
    def destroy_table(self):
        dpg.delete_item("wallet_tabbuild_parameterle")

    def callback_wallet(self):
        wallet_window.window.switch_visibility()

    def callback_wallet_add(self):
        new_add = dpg.get_value("wallet_new_add")
        new_ip = dpg.get_value("wallet_new_ip")
        #wallet_logic.add_new_item(new_add, new_ip)
        #dpg.set_value("wallet_new_add", "")
        #dpg.set_value("wallet_new_ip", "")
        #wallet_window.window.destroy_table()
        #wallet_window.window.build_table()

    def callback_wallet_remove(self):
        wallet_logic.remoprocessing_item_id(sender)
        #wallet_window.window.destroy_table()
        #wallet_window.window.build_table()
