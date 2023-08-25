#---------------------------------------------
from src.scheme.utils import scheme_function
from src.scheme.utils import scheme_connection

import dearpygui.dearpygui as dpg


def design_block():
    with dpg.node(label="Cloud", tag="node_block_cloud"):
        scheme_function.add_image("icon_cloud", "icon_cloud_visible")
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.drawlist(tag="block_cloud", width=225, height=250):
                pass

def design_node():
    with dpg.node(label="cloud_car", tag="node_cloud_car"):
        scheme_function.add_ip("va_ip")
        scheme_connection.add_http_client_i("va_http_client")
