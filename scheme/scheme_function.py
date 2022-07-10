#! /usr/bin/python
#---------------------------------------------

from param import param_py
from param import param_co

from scheme import scheme_callback

import dearpygui.dearpygui as dpg

color_line = (255, 255, 255, 50)
color_info = (0, 200, 200)
color_status = (0, 200, 50)

# Generic stuff
def line():
    with dpg.drawlist(width=125, height=1):
        dpg.draw_line([0, 0], [125, 0], color=color_line)
def add_attribute(text):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        dpg.add_text(text);
def add_variable(text, tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        line()
        with dpg.group(horizontal=True):
            dpg.add_text(text);
            dpg.add_text(0, tag=tag_, color=color_info);
def add_input(text, tag_):
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        line()
        dpg.add_text(text);
def add_output(text, tag_):
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        line()
        dpg.add_text(text);
def add_status(tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Status:");
            dpg.add_text("-", tag=tag_, color=color_status);
def add_ip(tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("IP:");
            dpg.add_text("127.0.0.1", tag=tag_, color=color_info);
def add_port(tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Port:");
            a = dpg.add_text(1, tag=tag_, color=color_info);
            dpg.add_button(arrow=True, direction=dpg.mvDir_Left, user_data=a, callback=lambda s, a, u: dpg.set_value(u, int(dpg.get_value(u))-1))
            dpg.add_button(arrow=True, direction=dpg.mvDir_Right, user_data=a, callback=lambda s, a, u: dpg.set_value(u, int(dpg.get_value(u))+1))

# Specific stuff
def add_false_alarm():
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        dpg.add_button(label="False alarm", tag="but_fal", callback=scheme_callback.callback_false_alarm)
def add_choice_edge():
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        edges = ("France_1", "France_2", "Spain_1")
        dpg.add_combo(edges, tag="combo_edge", label="Edge", default_value="France_1", width=125, callback=scheme_callback.callback_false_alarm)
def add_stockage(tag_):
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        line()
        dpg.add_text("Stockage")
def add_geolocalization():
    with dpg.node_attribute(tag="geo_input", attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        with dpg.group(horizontal=True):
            dpg.add_text("Geo: [")
            dpg.add_text(param_py.geo_country, color=color_info)
            dpg.add_text("]")

# Lidar stuff
def add_lidar_device(text, devices, default, tag_con, tag_list):
    with dpg.node_attribute(tag=tag_con, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        dpg.add_text(text)
        dpg.add_listbox(devices, tag=tag_list, callback=scheme_callback.callback_choice_device, default_value=default, width=150, num_items=len(devices))
def add_lidar(label, tag_con, tag_active, tag_speed, tag_ip, tag_packet):
    with dpg.node_attribute(tag=tag_con, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        line()
        with dpg.group(horizontal=True):
            dpg.add_text(label);
            dpg.add_checkbox(tag=tag_active, label="", default_value=True, callback=scheme_callback.callback_ssd);
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Speed:");
            dpg.add_input_int(tag=tag_speed, label="", default_value=600, step=60, min_value=0, max_value=1200, width=100, min_clamped=True, max_clamped=True, callback=scheme_callback.callback_lidar);
        with dpg.group(horizontal=True):
            dpg.add_text("IP:");
            dpg.add_input_text(tag=tag_ip, label="", default_value="", width=200, callback=scheme_callback.callback_lidar);
        with dpg.group(horizontal=True):
            dpg.add_button(label="Start")
            dpg.add_button(label="Stop")
        with dpg.group(horizontal=True):
            dpg.add_text("Packet:");
            dpg.add_text(0, tag=tag_packet, color=color_info);

# MQTT stuff
def add_mqtt(tag_):
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        dpg.add_text("MQTT");
def add_topic(tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Topic");
            dpg.add_text("-", tag= tag_, color=color_info);

# SSD stuff
def add_ssd(tag_con, tag_active, tag_path, tag_path_add, tag_used, tag_tot):
    with dpg.node_attribute(tag=tag_con, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        with dpg.group(horizontal=True):
            dpg.add_text("SSD");
            dpg.add_checkbox(tag=tag_active, label="", default_value=True, callback=scheme_callback.callback_ssd);
        with dpg.group(horizontal=True):
            dpg.add_text("-", tag=tag_path, color=color_info)
        with dpg.group(horizontal=True):
            dpg.add_input_text(tag=tag_path_add, label="", default_value="", width=150, callback=scheme_callback.callback_ssd);
        with dpg.group(horizontal=True):
            dpg.add_text("Size:");
            dpg.add_text(0, tag=tag_used, color=color_info);
            dpg.add_text("/");
            dpg.add_text(0, tag=tag_tot, color=color_info);
            dpg.add_text("Gb");
def add_file_info(label, tag_path, tag_size):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        line()
        dpg.add_text(label)
        with dpg.group(horizontal=True):
            dpg.add_text("-", tag=tag_path, color=color_info)
        with dpg.group(horizontal=True):
            dpg.add_text("Size:")
            dpg.add_text(0, tag=tag_size, color=color_info)
            dpg.add_text("Gb");
