#---------------------------------------------
from src.element.cloud.operator import operator_function
from src.element.base import node
import dearpygui.dearpygui as dpg


class Car_node(node.Node):
    def build(self):
        with dpg.node(label="cloud_car", tag="car_node"):
            with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
                with dpg.group(horizontal=True):
                    dpg.add_text("IP:");
                    dpg.add_text("127.0.0.1", tag="car_ip", color=gui_color.color_info);
            with dpg.node_attribute(tag="car_http_client", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
                with dpg.group(horizontal=True):
                    dpg.add_text("HTTPS");
                    dpg.add_text("client", color=gui_color.color_info);
