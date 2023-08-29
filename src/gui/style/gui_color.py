#---------------------------------------------
import dearpygui.dearpygui as dpg


color_info = (0, 200, 200)
color_title = (200, 200, 200)
color_line = (255, 255, 255, 50)
color_status = (0, 200, 50)
color_grey = (150, 150, 150)

color_node_value = (154, 175, 219)
color_node_sub = (0, 200, 200)


def color_checkbox():
    color_1 = (255, 255, 255)
    color_2 = (0, 0, 0)
    theme = dpg.add_theme()
    with dpg.theme_component(dpg.mvAll, parent=theme):
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
def theme_node_sub():
    theme = dpg.add_theme()
    with dpg.theme_component(dpg.mvAll, parent=theme):
        color_2 = (0, 0, 0)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, color_2, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, color_2, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, color_2, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Text, color_node_sub, category=dpg.mvThemeCat_Core)
    return theme
def theme_node_value():
    theme = dpg.add_theme()
    with dpg.theme_component(dpg.mvAll, parent=theme):
        color_2 = (0, 0, 0)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, color_2, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, color_2, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, color_2, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Text, color_node_value, category=dpg.mvThemeCat_Core)
    return theme
def color_yaxis_0():
    yaxis = dpg.add_theme()
    with dpg.theme_component(dpg.mvAll, parent=yaxis):
        dpg.add_theme_color(dpg.mvPlotCol_Line, (100, 100, 100), category=dpg.mvThemeCat_Plots)
        dpg.add_theme_style(dpg.mvPlotStyleVar_LineWeight, 0.5, category=dpg.mvThemeCat_Plots)
    return yaxis
def color_window_info():
    color = (60, 60, 60)
    black = (0, 0, 0)
    white = (255, 255, 255)
    theme = dpg.add_theme()
    with dpg.theme_component(dpg.mvAll, parent=theme):
        dpg.add_theme_color(dpg.mvThemeCol_ChildBg, color, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Text, white, category=dpg.mvThemeCat_Core)
    return theme

def color_block_ground():
    color = (10, 40, 100, 30)
    layer_control = dpg.add_theme()
    with dpg.theme_component(dpg.mvNode, parent=layer_control):
        dpg.add_theme_color(dpg.mvNodeCol_TitleBar, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBarHovered, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBarSelected, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_NodeBackground, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_NodeBackgroundHovered, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_NodeBackgroundSelected, color, category=dpg.mvThemeCat_Nodes)
    return layer_control
def color_block_edge():
    color = (45, 108, 143, 30)
    layer_control = dpg.add_theme()
    with dpg.theme_component(dpg.mvNode, parent=layer_control):
        dpg.add_theme_color(dpg.mvNodeCol_TitleBar, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBarHovered, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBarSelected, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_NodeBackground, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_NodeBackgroundHovered, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_NodeBackgroundSelected, color, category=dpg.mvThemeCat_Nodes)
    return layer_control
def color_block_cloud():
    color = (34, 133, 109, 30)
    layer_control = dpg.add_theme()
    with dpg.theme_component(dpg.mvNode, parent=layer_control):
        dpg.add_theme_color(dpg.mvNodeCol_TitleBar, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBarHovered, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBarSelected, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_NodeBackground, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_NodeBackgroundHovered, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_NodeBackgroundSelected, color, category=dpg.mvThemeCat_Nodes)
    return layer_control

def color_buton_red():
    red = (200, 50, 20)
    theme = dpg.add_theme()
    with dpg.theme_component(dpg.mvAll, parent=theme):
        dpg.add_theme_color(dpg.mvThemeCol_Button, red, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, red, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, red, category=dpg.mvThemeCat_Core)
    return theme
def color_buton_green():
    green = (20, 200, 20)
    theme = dpg.add_theme()
    with dpg.theme_component(dpg.mvAll, parent=theme):
        dpg.add_theme_color(dpg.mvThemeCol_Button, green, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, green, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, green, category=dpg.mvThemeCat_Core)
        return theme
def color_buton_gray():
    green = (100, 100, 100)
    theme = dpg.add_theme()
    with dpg.theme_component(dpg.mvAll, parent=theme):
        dpg.add_theme_color(dpg.mvThemeCol_Button, green, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, green, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, green, category=dpg.mvThemeCat_Core)
    return theme

def color_text_red():
    color = (200, 50, 20)
    theme = dpg.add_theme()
    with dpg.theme_component(dpg.mvAll, parent=theme):
        dpg.add_theme_color(dpg.mvThemeCol_Text, color, category=dpg.mvThemeCat_Core)
    return theme
def color_text_green():
    color = (20, 200, 20)
    theme = dpg.add_theme()
    with dpg.theme_component(dpg.mvAll, parent=theme):
        dpg.add_theme_color(dpg.mvThemeCol_Text, color, category=dpg.mvThemeCat_Core)
    return theme

def color_buton_control():
    color = (100, 20, 20)
    theme = dpg.add_theme()
    with dpg.theme_component(dpg.mvAll, parent=theme):
        dpg.add_theme_color(dpg.mvThemeCol_Button, color, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, color, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, color, category=dpg.mvThemeCat_Core)
    return theme
def color_buton_train():
    color = (14, 58, 125)
    theme = dpg.add_theme()
    with dpg.theme_component(dpg.mvAll, parent=theme):
        dpg.add_theme_color(dpg.mvThemeCol_Button, color, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, color, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, color, category=dpg.mvThemeCat_Core)
    return theme
def color_buton_edge():
    color = (45, 108, 143)
    theme = dpg.add_theme()
    with dpg.theme_component(dpg.mvAll, parent=theme):
        dpg.add_theme_color(dpg.mvThemeCol_Button, color, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, color, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, color, category=dpg.mvThemeCat_Core)
    return theme
def color_buton_cloud():
    color = (34, 133, 109)
    theme = dpg.add_theme()
    with dpg.theme_component(dpg.mvAll, parent=theme):
        dpg.add_theme_color(dpg.mvThemeCol_Button, color, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, color, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, color, category=dpg.mvThemeCat_Core)
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
def color_layer_train():
    color = (10, 40, 100)
    layer_train = dpg.add_theme()
    with dpg.theme_component(dpg.mvNode, parent=layer_train):
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
        color = (34, 133, 109)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBar, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBarHovered, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBarSelected, color, category=dpg.mvThemeCat_Nodes)
    return layer_cloud
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
def color_layer_legend():
    layer_cloud = dpg.add_theme()
    with dpg.theme_component(dpg.mvNode, parent=layer_cloud):
        color = (0, 0, 0)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBar, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBarHovered, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBarSelected, color, category=dpg.mvThemeCat_Nodes)
    return layer_cloud
def color_layer_network():
    layer_cloud = dpg.add_theme()
    with dpg.theme_component(dpg.mvNode, parent=layer_cloud):
        color = (0, 0, 0)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBar, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBarHovered, color, category=dpg.mvThemeCat_Nodes)
        dpg.add_theme_color(dpg.mvNodeCol_TitleBarSelected, color, category=dpg.mvThemeCat_Nodes)
    return layer_cloud
