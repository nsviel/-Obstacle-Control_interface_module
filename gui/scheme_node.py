#! /usr/bin/python
#---------------------------------------------

from param import param_co
from param import param_py
from param import param_hu
from param import param_li

from gui import scheme_callback

import dearpygui.dearpygui as dpg

color_status = (0, 200, 50)
color_info = (0, 200, 200)
color_line = (255, 255, 255, 50)

coord_controlium = [250, 350]
coord_pywardium = [250, 10]
coord_hubium = [525, 100]
coord_train = [10, 10]
coord_edge = [825, 300]
coord_local = [825, 10]
coord_sncf = [825, 150]
coord_valeo = [10, 200]


def node_controlium():
    with dpg.node(label="Controlium", tag="node_co", pos=coord_controlium):
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("Status:");
                dpg.add_text(param_co.status, tag="co_status", color=color_status);
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("IP:");
                dpg.add_text(param_py.pywardium_ip, color=color_info);

        with dpg.node_attribute(tag="co_http_client", attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
            line()
            dpg.add_text("HTTP client");
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            dpg.add_button(label="False alarm", tag="but_fal", callback=scheme_callback.callback_false_alarm)
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            dpg.add_button(label="Change Edge", tag="but_ched", callback=scheme_callback.callback_false_alarm)

def node_pywardium():
    with dpg.node(label="Pywardium", tag="node_py", pos=coord_pywardium):
        with dpg.node_attribute(tag="py_server", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            with dpg.group(horizontal=True):
                dpg.add_text("Status:");
                dpg.add_text(param_py.status, tag="py_status", color=color_status);
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("IP:");
                dpg.add_text(param_py.pywardium_ip, color=color_info);

        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            line()
            dpg.add_text("Pcapy");
        with dpg.node_attribute(tag="py_device_l1", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            with dpg.group(horizontal=True):
                dpg.add_text("Device:");
                dpg.add_text(param_li.device_l1, tag="py_device_l1_val", color=color_info);
        with dpg.node_attribute(tag="py_device_l2", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            with dpg.group(horizontal=True):
                dpg.add_text("Device:");
                dpg.add_text(param_li.device_l2, tag="py_device_l2_val", color=color_info);

        with dpg.node_attribute(tag="py_sock_client", attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
            line()
            dpg.add_text("Socket client");
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("Port:");
                dpg.add_text(param_hu.hubium_httpd_port, tag="py_port_sock_val", color=color_info);

        with dpg.node_attribute(tag="py_http_server", attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
            line()
            dpg.add_text("HTTP server");
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("Port:");
                dpg.add_text(param_py.http_port, tag="py_http_server_val", color=color_info);

def node_hubium():
    with dpg.node(label="Hubium", tag="node_hu", pos=coord_hubium):
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("Status:");
                dpg.add_text(param_hu.hubium_status, tag="hu_status", color=color_status);
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("IP:");
                dpg.add_text(param_hu.hubium_ip, color=color_info);

        with dpg.node_attribute(tag="hu_stockage", attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
            line()
            dpg.add_text("Stockage")
        with dpg.node_attribute(tag="hu_mqtt", attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
            dpg.add_text("MQTT");

        with dpg.node_attribute(tag="hu_sock_client", attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
            line()
            dpg.add_text("Socket client");
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("Port:");
                dpg.add_text(param_hu.hubium_sock_connection, tag="hu_sock_client_val", color=color_info);

        with dpg.node_attribute(tag="hu_sock_server_in", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            line()
            dpg.add_text("Socket server");
        with dpg.node_attribute(tag="hu_sock_server_out", attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
            with dpg.group(horizontal=True):
                dpg.add_text("Port:");
                dpg.add_text(param_hu.hubium_sock_port, tag="hu_sock_server_val", color=color_info);

        with dpg.node_attribute(tag="hu_http_client", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            line()
            dpg.add_text("HTTP client");
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("Port:");
                dpg.add_text(param_hu.hubium_httpd_port, tag="hu_http_client_val", color=color_info);

        with dpg.node_attribute(tag="hu_http_server", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            line()
            dpg.add_text("HTTP server");
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("Port:");
                dpg.add_text(param_hu.hubium_httpd_port, tag="hu_http_server_val", color=color_info);

def node_train():
    with dpg.node(label="Train", tag="node_train", pos=coord_train):
        with dpg.node_attribute(tag="geo_input", attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
            with dpg.group(horizontal=True):
                dpg.add_text("Geo: [")
                dpg.add_text(param_py.geo_country, color=color_info)
                dpg.add_text("]")
        with dpg.node_attribute(tag="ssd_input", attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
            with dpg.group(horizontal=True):
                dpg.add_text("SSD:");
                dpg.add_text(param_py.ssd_space_used, tag="ssd_used", color=color_info);
                dpg.add_text("/");
                dpg.add_text(param_py.ssd_space_total, tag="ssd_total", color=color_info);
                dpg.add_text("Gb");
        with dpg.node_attribute(tag="l1_input", attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
            line()
            with dpg.group(horizontal=True):
                dpg.add_text("Lidar 1:");
                dpg.add_button(label="Start")
                dpg.add_button(label="Stop")
                dpg.add_text(param_li.nb_packet_l1, tag="l1_packet", color=color_info);
        with dpg.node_attribute(tag="l2_input", attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
            with dpg.group(horizontal=True):
                dpg.add_text("Lidar 2:");
                dpg.add_button(label="Start")
                dpg.add_button(label="Stop")
                dpg.add_text(param_li.nb_packet_l2, tag="l2_packet", color=color_info);

def node_edge():
    with dpg.node(label="Edge", tag="node_ed", pos=coord_edge):
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("IP:");
                dpg.add_text(param_hu.edge_ip, color=color_info);

        with dpg.node_attribute(tag="ed_client", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            line()
            dpg.add_text("Socket client");
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("Port:");
                dpg.add_text(param_hu.edge_port, tag="ed_port_client", color=color_info);

        with dpg.node_attribute(tag="ed_server", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            line()
            dpg.add_text("Socket server")
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("Port:");
                dpg.add_text(param_hu.edge_port, tag="ed_port", color=color_info);

        with dpg.node_attribute(tag="ed_http_server", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            line()
            dpg.add_text("HTTP server");
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("Port:");
                dpg.add_text(param_hu.hubium_httpd_port, tag="ed_http_server_val", color=color_info);

def node_edge_local():
    with dpg.node(label="Local", tag="node_local", pos=coord_local):
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            dpg.add_text("Velodium");
        with dpg.node_attribute(tag="ve_input", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            dpg.add_text("Socket server");
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("Port:");
                dpg.add_text(param_hu.hubium_httpd_port, tag="ve_port", color=color_info);

        with dpg.node_attribute(tag="ai_input", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            line()
            dpg.add_text("AI");

def node_sncf():
    with dpg.node(label="SNCF", tag="node_sncf", pos=coord_sncf):
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("IP:");
                dpg.add_text(param_hu.mqtt_ip, color=color_info);

        with dpg.node_attribute(tag="sncf_mqtt_port", attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
            line()
            dpg.add_text("MQTT");
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("Topic");
                dpg.add_text(param_hu.mqtt_topic, color=color_info);
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("Port:");
                dpg.add_text(param_hu.mqtt_port, tag="sncf_port", color=color_info);

def node_valeo():
    with dpg.node(label="Valeo", tag="node_valeo", pos=coord_valeo):
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.group(horizontal=True):
                dpg.add_text("IP:");
                dpg.add_text(param_hu.valeo_ip, color=color_info);

        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            line()
            dpg.add_text("HTTP");
        with dpg.node_attribute(tag="va_httpd_port", attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
            with dpg.group(horizontal=True):
                dpg.add_text("Port:");
                dpg.add_text(param_hu.mqtt_port, tag="va_port", color=color_info);

def line():
    with dpg.drawlist(width=125, height=1):
        dpg.draw_line([0, 0], [125, 0], color=color_line)
