#! /usr/bin/python
#---------------------------------------------

import dearpygui.dearpygui as dpg


def color_red():
    red = dpg.add_theme()
    with dpg.theme_component(dpg.mvNodeLink, parent=red):
        color = (255, 20, 20)
        dpg.add_theme_color(dpg.mvNodeCol_Link, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_LinkHovered, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_LinkSelected, color, category=dpg.mvThemeCat_Nodes)
    return red

def color_green():
    green = dpg.add_theme()
    with dpg.theme_component(dpg.mvNodeLink, parent=green):
        color = (20, 255, 20)
        dpg.add_theme_color(dpg.mvNodeCol_Link, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_LinkHovered, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_LinkSelected, color, category=dpg.mvThemeCat_Nodes)
    return green

def color_layer_control():
    layer_control = dpg.add_theme()
    with dpg.theme_component(dpg.mvNode, parent=layer_control):
        color = (100, 20, 20)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBar, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBarHovered, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBarSelected, color, category=dpg.mvThemeCat_Nodes)
    return layer_control

def color_layer_train():
    layer_train = dpg.add_theme()
    with dpg.theme_component(dpg.mvNode, parent=layer_train):
        color = (20, 82, 175)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBar, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBarHovered, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBarSelected, color, category=dpg.mvThemeCat_Nodes)
    return layer_train

def color_layer_edge():
    layer_edge = dpg.add_theme()
    with dpg.theme_component(dpg.mvNode, parent=layer_edge):
        color = (45, 108, 143)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBar, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBarHovered, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBarSelected, color, category=dpg.mvThemeCat_Nodes)
    return layer_edge

def color_layer_cloud():
    layer_cloud = dpg.add_theme()
    with dpg.theme_component(dpg.mvNode, parent=layer_cloud):
        color = (106, 106, 105)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBar, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBarHovered, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBarSelected, color, category=dpg.mvThemeCat_Nodes)
    return layer_cloud
