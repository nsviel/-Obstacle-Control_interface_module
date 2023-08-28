#---------------------------------------------
from src.gui.background import gui_ID
import dearpygui.dearpygui as dpg


class Block_ground:
    def __init__(self, ID):
        self.ID = ID

    def design_block(self):
        with dpg.node(label="Ground", tag=self.ID.ID_block_ground, draggable=True):
            with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
                dpg.add_image(self.ID.ID_icon_ground, width=25, height=30)
                dpg.add_text("")
            with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
                with dpg.drawlist(width=450, height=200):
                    pass

    def set_visibility(self, what):
        if(what == False):
            dpg.hide_item(self.ID.ID_block_ground)
        elif(what == True):
            dpg.show_item(self.ID.ID_block_ground)
