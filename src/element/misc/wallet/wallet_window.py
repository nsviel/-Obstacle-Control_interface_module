#---------------------------------------------
from src.param import param_control
from src.element.misc.wallet import wallet_window
from src.gui.style import gui_color
from src.base import window
import dearpygui.dearpygui as dpg
import json


class Wallet_window(window.Window):
    def __init__(self, ID, logic):
        self.ID = ID
        self.logic = logic

    # Build function
    def build_parameter(self):
        self.build_add_element()
        self.build_list_element()
    def build_add_element(self):
        with dpg.table(header_row=False):
            dpg.add_table_column()
            dpg.add_table_column()
            with dpg.table_row():
                dpg.add_text("New element", color=(150, 150, 150));
                dpg.add_button(label="Add item", callback=self.add_new_add)
        with dpg.group(horizontal=True):
            dpg.add_text("Address")
            dpg.add_input_text(tag=self.ID.ID_new_address, label="", width=200)
        with dpg.group(horizontal=True):
            dpg.add_text("IP: ")
            dpg.add_input_text(tag=self.ID.ID_new_ip, label="", width=200)
    def build_list_element(self):
        with dpg.table(tag=self.ID.ID_table, header_row=True, borders_innerH=True, borders_outerH=True, parent=self.ID.ID_window_parameter, policy=dpg.mvTable_SizingFixedFit):
            dpg.add_table_column(label="Address")
            dpg.add_table_column(label="IP")
            dpg.add_table_column(label="", width_fixed=True, init_width_or_weight=20)
            for i in range(len(self.logic.get_list_add())):
                with dpg.table_row():
                    dpg.add_text(self.logic.get_list_add()[i])
                    dpg.add_text(list(self.logic.wallet.values())[i])
                    if(i > 6):
                        dpg.add_button(label="X", tag=str(i), callback=self.remove_add)
    def rebuild_list_element(self):
        dpg.delete_item(self.ID.ID_table,)
        self.build_list_element()

    # Subfunction
    def add_new_add(self):
        # Get new address
        new_add = dpg.get_value(self.ID.ID_new_address)
        dpg.set_value(self.ID.ID_new_address, "")

        # Get new IP
        new_ip = dpg.get_value(self.ID.ID_new_ip)
        dpg.set_value(self.ID.ID_new_ip, "")

        # Create address ad rebuild list
        self.logic.add_new_item(new_add, new_ip)
        self.rebuild_list_element()
    def remove_add(self, sender):
        self.logic.remove_item_id(sender)
        self.rebuild_list_element()

    # Update function
    def update(self):
        pass
