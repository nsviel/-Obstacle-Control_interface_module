#! /usr/bin/python
#---------------------------------------------

import dearpygui.dearpygui as dpg


def color_checkbox():
    theme = dpg.add_theme()
    with dpg.theme_component(dpg.mvAll, parent=theme):
        color_1 = (255, 255, 255)
        color_2 = (0, 0, 0)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, color_2, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, color_2, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, color_2, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_CheckMark, color_1, category=dpg.mvThemeCat_Core)
    return theme
def color_input_text():
    theme = dpg.add_theme()
    with dpg.theme_component(dpg.mvAll, parent=theme):
        color_1 = (0, 200, 200)
        color_2 = (0, 0, 0)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, color_2, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, color_2, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, color_2, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Text, color_1, category=dpg.mvThemeCat_Core)
    return theme
def color_yaxis_0():
    yaxis = dpg.add_theme()
    with dpg.theme_component(dpg.mvAll, parent=yaxis):
        dpg.add_theme_color(dpg.mvPlotCol_Line, (100, 100, 100), category=dpg.mvThemeCat_Plots)
        dpg.add_theme_style(dpg.mvPlotStyleVar_LineWeight, 0.5, category=dpg.mvThemeCat_Plots)
    return yaxis

def color_status_red():
    theme = dpg.add_theme()
    with dpg.theme_component(dpg.mvAll, parent=theme):
        red = (255, 50, 20)
        black = (0, 0, 0)
        dpg.add_theme_color(dpg.mvThemeCol_Button, red, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, red, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, red, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Text, red, category=dpg.mvThemeCat_Core)
    return theme
def color_status_green():
    theme = dpg.add_theme()
    with dpg.theme_component(dpg.mvAll, parent=theme):
        green = (20, 255, 20)
        black = (0, 0, 0)
        dpg.add_theme_color(dpg.mvThemeCol_Button, green, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, green, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, green, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Text, green, category=dpg.mvThemeCat_Core)
    return theme

def color_link_red():
    red = dpg.add_theme()
    with dpg.theme_component(dpg.mvNodeLink, parent=red):
        color = (255, 50, 20)
        dpg.add_theme_color(dpg.mvNodeCol_Link, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_LinkHovered, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_LinkSelected, color, category=dpg.mvThemeCat_Nodes)
    return red
def color_link_green():
    green = dpg.add_theme()
    with dpg.theme_component(dpg.mvNodeLink, parent=green):
        color = (20, 255, 20)
        dpg.add_theme_color(dpg.mvNodeCol_Link, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_LinkHovered, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_LinkSelected, color, category=dpg.mvThemeCat_Nodes)
    return green
def color_link_blue():
    green = dpg.add_theme()
    with dpg.theme_component(dpg.mvNodeLink, parent=green):
        color = (20, 20, 255)
        dpg.add_theme_color(dpg.mvNodeCol_Link, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_LinkHovered, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_LinkSelected, color, category=dpg.mvThemeCat_Nodes)
    return green
def color_link_whiteblue():
    green = dpg.add_theme()
    with dpg.theme_component(dpg.mvNodeLink, parent=green):
        color = (255, 255, 255)
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
def color_layer_stat():
    layer_control = dpg.add_theme()
    with dpg.theme_component(dpg.mvNode, parent=layer_control):
        color = (0, 0, 0, 0)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBar, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBarHovered, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBarSelected, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_NodeBackground, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_NodeBackgroundHovered, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_NodeBackgroundSelected, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_NodeOutline, color, category=dpg.mvThemeCat_Nodes)
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
