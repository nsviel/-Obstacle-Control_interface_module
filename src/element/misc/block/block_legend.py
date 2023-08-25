#---------------------------------------------
import dearpygui.dearpygui as dpg


class Block_legend:
    def __init__(self, ID):
        self.ID = ID

    def design_block(self):
        with dpg.node(label="Legend", tag=self.ID.ID_block_legend):
            self.add_legend_line(self.ID.ID_legend_ground, "Train level components")
            self.add_legend_line(self.ID.ID_legend_edge, "Edge level components")
            self.add_legend_line(self.ID.ID_legend_cloud, "Cloud level components")
            self.add_legend_line(self.ID.ID_legend_control, "Control level components")

    def add_legend_line(tag_button, text):
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_button(tag=tag_button, width=15)
                dpg.add_text(": " + text);
