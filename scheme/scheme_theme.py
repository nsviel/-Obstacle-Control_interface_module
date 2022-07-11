#! /usr/bin/python
#---------------------------------------------

from scheme import scheme_color

import dearpygui.dearpygui as dpg

color_node_grid_line = (30, 30, 30)
color_node_grid_bkg = (40, 40, 40)
color_node_bkg = (25, 25, 25)
color_node_pin = (200, 200, 10)
color_node_link = (255, 255, 255)


def global_theme():
    with dpg.theme() as global_theme:
        with dpg.theme_component(dpg.mvAll):
            # Divers
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (20, 20, 20), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Button, (100, 100, 100))
            dpg.add_theme_color(dpg.mvThemeCol_MenuBarBg, (0, 0, 0))

            # Node background
            dpg.add_theme_color(dpg.mvNodeCol_NodeBackground, color_node_bkg, category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_NodeBackgroundHovered, color_node_bkg, category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_NodeBackgroundSelected, color_node_bkg, category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_NodeOutline, (0, 0, 0), category=dpg.mvThemeCat_Nodes)

            # Node link
            dpg.add_theme_color(dpg.mvNodeCol_Link, color_node_link, category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_LinkHovered, color_node_link, category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_LinkSelected, color_node_link, category=dpg.mvThemeCat_Nodes)

            # Node pin
            dpg.add_theme_color(dpg.mvNodeCol_Pin, color_node_pin, category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_PinHovered, color_node_pin, category=dpg.mvThemeCat_Nodes)

            # Node grid
            dpg.add_theme_color(dpg.mvNodeCol_GridBackground, color_node_grid_bkg, category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_GridLine, color_node_grid_line, category=dpg.mvThemeCat_Nodes)

            # Node box selector
            dpg.add_theme_color(dpg.mvNodeCol_BoxSelector, (0, 0, 0, 100), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_BoxSelectorOutline, (175, 175, 175), category=dpg.mvThemeCat_Nodes)

    dpg.bind_theme(global_theme)

def colorize():
    colorize_node()
    colorize_item()

def colorize_node():
    layer_control = scheme_color.color_layer_control()
    layer_train = scheme_color.color_layer_train()
    layer_edge = scheme_color.color_layer_edge()
    layer_cloud = scheme_color.color_layer_cloud()

    dpg.bind_item_theme("node_co", layer_control)
    dpg.bind_item_theme("node_py", layer_train)
    dpg.bind_item_theme("node_train", layer_train)
    dpg.bind_item_theme("node_hu", layer_edge)
    dpg.bind_item_theme("node_local", layer_edge)
    dpg.bind_item_theme("node_ed", layer_cloud)
    dpg.bind_item_theme("node_sncf", layer_cloud)
    dpg.bind_item_theme("node_valeo", layer_cloud)
    dpg.bind_item_theme("node_ssd", layer_control)

def colorize_item():
    checkbox = scheme_color.color_checkbox()
    input_text = scheme_color.color_input_text()

    dpg.bind_item_theme("ssd_active", checkbox)
    dpg.bind_item_theme("l1_active", checkbox)
    dpg.bind_item_theme("l2_active", checkbox)
    dpg.bind_item_theme("ssd_path_add", input_text)
    dpg.bind_item_theme("ssd_path", input_text)
