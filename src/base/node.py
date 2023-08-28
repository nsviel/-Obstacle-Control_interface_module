#---------------------------------------------
from src.gui.style import colorization
from src.gui.style import gui_color
from src.utils import parser_json
import dearpygui.dearpygui as dpg


class Node:
    def __init__(self, ID):
        self.ID = ID
        self.status = "Offline"
        self.is_visible = True

    # Design
    def build(self):
        pass

    # Update
    def set_visibility(self, value):
        if(value == False):
            dpg.hide_item(self.ID.ID_node)
            self.is_visible = False
        elif(value == True):
            dpg.show_item(self.ID.ID_node)
            self.is_visible = True
