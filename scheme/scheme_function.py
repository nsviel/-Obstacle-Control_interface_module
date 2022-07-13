#! /usr/bin/python
#---------------------------------------------

from scheme import scheme_callback

from math import sin

import dearpygui.dearpygui as dpg

color_line = (255, 255, 255, 50)
color_info = (0, 200, 200)
color_status = (0, 200, 50)
color_title = (200, 200, 200)


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
def add_variable_simple(text, tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text(text);
            dpg.add_text(0, tag=tag_, color=color_info);
def add_input(text, tag_):
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        line()
        dpg.add_text(text, color=color_title);
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
def add_port_fixe(tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Port:");
            dpg.add_text(1, tag=tag_, color=color_info);
def add_plot():
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        # creating data
        sindatax = []
        sindatay = []
        for i in range(0, 500):
            sindatax.append(i / 1000)
            sindatay.append(0.5 + 0.5 * sin(50 * i / 1000))

        # create plot
        with dpg.plot(label="Line Series", height=150, width=300):
            dpg.add_plot_axis(dpg.mvXAxis, label="x")
            dpg.add_plot_axis(dpg.mvYAxis, label="y", tag="y_axis")
            dpg.add_line_series(sindatax, sindatay, label="0.5 + 0.5 * sin(x)", parent="y_axis")

# Specific stuff
def add_false_alarm(tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        dpg.add_button(label="False alarm", tag=tag_, callback=scheme_callback.callback_false_alarm)
def add_choice_edge(tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        edges = ("France_1", "France_2", "Spain_1")
        dpg.add_combo(edges, tag=tag_, label="Edge", default_value="France_1", width=125, callback=scheme_callback.callback_false_alarm)
def add_stockage(tag_):
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        line()
        dpg.add_text("Stockage")
def add_geolocalization(tag_):
    with dpg.node_attribute(tag="geo_input", attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        with dpg.group(horizontal=True):
            dpg.add_text("Geo: [")
            dpg.add_text("", tag=tag_, color=color_info)
            dpg.add_text("]")
def add_image(tag):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        dpg.add_image(tag, width=300, height=175)

# Lidar stuff
def add_lidar_device(tag_l1_in, tag_l2_in, tag_l1_out, tag_l2_out, tag_l1_dev, tag_l2_dev):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        line()
        dpg.add_text("device", color=color_title)
    with dpg.node_attribute(tag=tag_l1_in, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        pass
    with dpg.node_attribute(tag=tag_l1_out, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        pass
    with dpg.node_attribute(tag=tag_l2_in, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        pass
    with dpg.node_attribute(tag=tag_l2_out, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        pass
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            with dpg.group():
                dpg.add_text("Lidar 1")
                dpg.add_listbox(tag=tag_l1_dev, callback=scheme_callback.callback_param_py, width=125)
            with dpg.group():
                dpg.add_text("Lidar 2")
                dpg.add_listbox(tag=tag_l2_dev, callback=scheme_callback.callback_param_py, width=125)
def add_lidar(label, tag_con, tag_active, tag_speed, tag_ip, tag_packet):
    with dpg.node_attribute(tag=tag_con, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        line()
        with dpg.group(horizontal=True):
            dpg.add_text(label, color=color_title);
            dpg.add_checkbox(tag=tag_active, label="", default_value=True, indent=75, callback=scheme_callback.callback_ssd);
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        #Speed
        with dpg.group(horizontal=True):
            dpg.add_text("Speed:");
            dpg.add_input_int(tag=tag_speed, label="", default_value=600, step=60, min_value=0, max_value=1200, width=100, min_clamped=True, max_clamped=True, callback=scheme_callback.callback_lidar);
        #IP
        with dpg.group(horizontal=True):
            dpg.add_text("IP:");
            dpg.add_input_text(tag=tag_ip, label="", default_value="", width=200, callback=scheme_callback.callback_lidar);
        # Start / Stop
        with dpg.group(horizontal=True):
            dpg.add_button(label="Start")
            dpg.add_button(label="Stop")
        #Packet number
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
def add_ssd(tag_con, tag_active, tag_path, tag_name, tag_path_add, tag_used, tag_tot):
    with dpg.node_attribute(tag=tag_con, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        with dpg.group(horizontal=True):
            dpg.add_text("SSD");
            dpg.add_checkbox(tag=tag_active, label="", default_value=True, indent=75, callback=scheme_callback.callback_ssd)
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        dpg.add_input_text(tag=tag_path, label="", default_value="", width=200, callback=scheme_callback.callback_ssd)
        dpg.add_input_text(tag=tag_path_add, label="", default_value="", width=200, callback=scheme_callback.callback_ssd)
        with dpg.group(horizontal=True):
            dpg.add_text("File:")
            dpg.add_text("-", tag=tag_name, color=color_info)
        with dpg.group(horizontal=True):
            dpg.add_text("Used:");
            dpg.add_text(0, tag=tag_used, color=color_info);
            dpg.add_text("/");
            dpg.add_text(0, tag=tag_tot, color=color_info);
            dpg.add_text("Gb");
def add_file_info(label, tag_path, tag_size):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        line()
        dpg.add_text(label, color=color_title)
        with dpg.group(horizontal=True):
            dpg.add_text("-", tag=tag_path, color=color_info)
        with dpg.group(horizontal=True):
            dpg.add_text("Size:")
            dpg.add_text(0, tag=tag_size, color=color_info)
            dpg.add_text("Gb");
