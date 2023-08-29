#---------------------------------------------
import dearpygui.dearpygui as dpg


class Block_cloud:
    def __init__(self, ID):
        self.ID = ID

    def design_block(self):
        with dpg.node(label="Cloud", tag=self.ID.ID_block_cloud):
            with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
                dpg.add_image(self.ID.ID_icon_cloud, width=35, height=30)
                dpg.add_text("")
            with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
                with dpg.drawlist(width=375, height=300):
                    pass

    def set_visibility(self, what):
        if(what == False):
            dpg.hide_item(self.ID.ID_block_cloud)
        elif(what == True):
            dpg.show_item(self.ID.ID_block_cloud)
