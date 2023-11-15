#---------------------------------------------
from src.gui.style import gui_color
import dearpygui.dearpygui as dpg


def colorize_node(ID_node, layer_name):
    if(layer_name == "ground"):
        color = gui_color.color_layer_train()
    elif(layer_name == "edge"):
        color = gui_color.color_layer_edge()
    elif(layer_name == "cloud"):
        color = gui_color.color_layer_cloud()
    elif(layer_name == "network"):
        color = gui_color.color_layer_network()
    else:
        print("[error] Colorization name not good")
    dpg.bind_item_theme(ID_node, color)

def colorize_blocks(ID_block, type_name):
    if(type_name == "ground"):
        color = gui_color.color_block_ground()
    elif(type_name == "edge"):
        color = gui_color.color_block_edge()
    elif(type_name == "cloud"):
        color = gui_color.color_block_cloud()
    elif(type_name == "control"):
        color = gui_color.color_block_cloud()
    else:
        print("[error] Colorization name not good")
    dpg.bind_item_theme(ID_block, color)

def colorize_item(ID_item, type_name):
    if(type_name == "checkbox"):
        color = gui_color.color_checkbox()
    elif(type_name == "input_text"):
        color = gui_color.color_input_text()
    elif(type_name == "line_yaxis"):
        color = gui_color.color_yaxis_0()
    elif(type_name == "node_value"):
        color = gui_color.theme_node_value()
    elif(type_name == "node_sub"):
        color = gui_color.theme_node_sub()
    else:
        print("[error] Colorization name not good")
    dpg.bind_item_theme(ID_item, color)

def colorize_status_light(tag, value):
    on = gui_color.color_buton_green()
    off = gui_color.color_buton_red()
    if(value == "Online" or value == True):
        dpg.bind_item_theme(tag, on)
    elif(value == "Offline" or value == False):
        dpg.bind_item_theme(tag, off)
def colorize_status(tag, value):
    on = gui_color.color_text_green()
    off = gui_color.color_text_red()
    if(value == "Online" or value == True):
        dpg.bind_item_theme(tag, on)
    elif(value == "Offline" or value == False):
        dpg.bind_item_theme(tag, off)

def colorize_onoff(tag_on, tag_off, state):
    color_on = gui_color.color_buton_green()
    color_off = gui_color.color_buton_red()
    color_grey = gui_color.color_buton_gray()
    if(state == True):
        dpg.bind_item_theme(tag_on, color_on)
        dpg.bind_item_theme(tag_off, color_grey)
    elif(state == False):
        dpg.bind_item_theme(tag_on, color_grey)
        dpg.bind_item_theme(tag_off, color_off)

# Link colorization
def colorize_link_http(ID, state):
    if(state):
        connected = gui_color.color_link_green()
        dpg.bind_item_theme(ID, connected)
    else:
        disconnected = gui_color.color_link_red()
        dpg.bind_item_theme(ID, disconnected)

def colorize_link_socket(ID, state):
    if(state):
        connected = gui_color.color_link_blue()
        dpg.bind_item_theme(ID, connected)
    else:
        disconnected = gui_color.color_link_whiteblue()
        dpg.bind_item_theme(ID, disconnected)
