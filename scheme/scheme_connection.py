#---------------------------------------------
from scheme import scheme_function
from scheme import scheme_command

import dearpygui.dearpygui as dpg

color_line = (255, 255, 255, 50)
color_info = (0, 200, 200)
color_status = (0, 200, 50)
color_title = (200, 200, 200)


def add_sock_server(tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        scheme_function.line()
        dpg.add_text("Socket server");
def add_sock_server_i_text(text, tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        dpg.add_text(text, color=color_title);
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        dpg.add_text("Socket server");
def add_sock_server_i(tag_):
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        scheme_function.line()
        dpg.add_text("Socket server");
def add_sock_server_o(tag_):
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        scheme_function.line()
        dpg.add_text("Socket server");
def add_sock_server_io(tag_i, tag_o):
    with dpg.node_attribute(tag=tag_i, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        scheme_function.line()
        dpg.add_text("Socket server");
    with dpg.node_attribute(tag=tag_o, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        a=1

def add_sock_client_i(tag_):
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        scheme_function.line()
        dpg.add_text("Socket client");
def add_sock_client_o(tag_):
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        scheme_function.line()
        dpg.add_text("Socket client");
def add_sock_client_o_(tag_):
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        dpg.add_text("Socket client");
def add_sock_client_io(tag_i, tag_o):
    with dpg.node_attribute(tag=tag_i, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        scheme_function.line()
        dpg.add_text("Socket client");
    with dpg.node_attribute(tag=tag_o, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        a=1

def add_sock_client_source_i(tag_i, tag_source):
    with dpg.node_attribute(tag=tag_i, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        scheme_function.line()
        dpg.add_text("Socket client");
        with dpg.group(horizontal=True):
            dpg.add_text("Source:");
            dpg.add_text("Lidar 2", tag=tag_source, color=color_info)
def add_sock_client_source_io(tag_i, tag_o, tag_combo):
    with dpg.node_attribute(tag=tag_i, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        scheme_function.line()
        dpg.add_text("Socket client");
    with dpg.node_attribute(tag=tag_o, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        with dpg.group(horizontal=True):
            dpg.add_text("Source:");
            choice = ("Lidar 1", "Lidar 2")
            dpg.add_combo(choice, tag=tag_combo, label="", default_value="Lidar 1", width=80, callback=scheme_command.command_lidar_source)

def add_http_client_i(tag_):
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        scheme_function.line()
        dpg.add_text("HTTP client");
def add_http_client_o(tag_):
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        scheme_function.line()
        dpg.add_text("HTTP client");
def add_http_client_io(tag_i, tag_o):
    with dpg.node_attribute(tag=tag_i, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        scheme_function.line()
        dpg.add_text("HTTP client");
    with dpg.node_attribute(tag=tag_o, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        a=1

def add_http_server_i_text(text, tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        scheme_function.line()
        dpg.add_text(text, color=color_title);
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        dpg.add_text("HTTP server");
def add_http_server_i(tag_):
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        scheme_function.line()
        dpg.add_text("HTTP server");
def add_http_server_o(tag_):
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        scheme_function.line()
        dpg.add_text("HTTP server");
def add_http_server_io(tag_i, tag_o):
    with dpg.node_attribute(tag=tag_i, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        scheme_function.line()
        dpg.add_text("HTTP server");
    with dpg.node_attribute(tag=tag_o, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        a=1
