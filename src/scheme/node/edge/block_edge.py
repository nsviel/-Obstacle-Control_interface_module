#---------------------------------------------
from src.param import param_interface
from src.scheme.utils import scheme_function
from src.scheme.utils import scheme_connection

import dearpygui.dearpygui as dpg


def design_block():
    with dpg.node(label="Edge", tag="node_block_edge"):
        scheme_function.add_image("icon_server", "icon_server_visible")
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.drawlist(tag="block_edge", width=350, height=350):
                pass
