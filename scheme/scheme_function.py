#! /usr/bin/python
#---------------------------------------------

import dearpygui.dearpygui as dpg

color_line = (255, 255, 255, 50)
color_info = (0, 200, 200)
color_status = (0, 200, 50)


def line():
    with dpg.drawlist(width=125, height=1):
        dpg.draw_line([0, 0], [125, 0], color=color_line)

def add_port(value, tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Port:");
            a = dpg.add_text(value, tag=tag_, color=color_info);
            dpg.add_button(arrow=True, direction=dpg.mvDir_Left, user_data=a, callback=lambda s, a, u: dpg.set_value(u, int(dpg.get_value(u))-1))
            dpg.add_button(arrow=True, direction=dpg.mvDir_Right, user_data=a, callback=lambda s, a, u: dpg.set_value(u, int(dpg.get_value(u))+1))

def add_sock_server(tag_):
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        line()
        dpg.add_text("Socket server");

def add_status(value, tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Status:");
            dpg.add_text(value, tag=tag_, color=color_status);

def add_ip(value, tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("IP:");
            dpg.add_text(value, tag=tag_, color=color_info);
