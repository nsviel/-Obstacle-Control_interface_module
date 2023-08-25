#---------------------------------------------
from src.param import param_interface
from src.scheme.style import scheme_theme
from src.scheme.object import object

import dearpygui.dearpygui as dpg


def update_node_pos_dev():
    gui_width = param_interface.state_control["gui"]["width"]
    gui_height = param_interface.state_control["gui"]["height"]
    coord_module_interface = [1100, 600]
    coord_module_capture = [250, 10]
    coord_edge_1 = [725, 400]
    coord_edge_2 = [1150, 215]
    coord_train = [10, 10]
    coord_component_process = [400, 510]
    coord_ai = [400, 745]
    coord_trainope = [1150, 50]
    coord_cloud_car = [1150, 450]
    coord_ssd = [1325, 600]
    coord_data = [650, 10]
    coord_network = [10, 510]

    dpg.set_item_pos("node_control", coord_module_interface)
    dpg.set_item_pos(object.object.edge_1.ID_node, coord_edge_1)
    dpg.set_item_pos("node_capture", coord_module_capture)
    dpg.set_item_pos("node_train", coord_train)
    dpg.set_item_pos(object.object.edge_2.ID_node, coord_edge_2)
    dpg.set_item_pos("node_slam", coord_component_process)
    dpg.set_item_pos("node_ai", coord_ai)
    dpg.set_item_pos("node_operator", coord_trainope)
    dpg.set_item_pos("node_cloud_car", coord_cloud_car)
    dpg.set_item_pos("node_ssd", coord_ssd)
    dpg.set_item_pos("node_data", coord_data)
    dpg.set_item_pos("node_network", coord_network)

    dpg.set_viewport_width(gui_width)
    dpg.set_viewport_height(gui_height)
    scheme_theme.scheme_theme_dev()
def update_node_pos_demo_minimized():
    gui_width = 1350
    gui_height = 775
    coord_module_interface = [1175, 325]
    coord_module_capture = [290, 100]
    coord_edge_1 = [725, 40]
    coord_edge_2 = [725, 250]
    coord_train = [25, 100]
    coord_component_process = [850, 350]
    coord_ai = [850, 550]
    coord_trainope = [1110, 200]
    coord_ssd = [1400, 325]
    coord_data = [600, 475]
    coord_legend = [1110, 10]
    coord_network = [75, 450]
    coord_block_train = [10, 10]
    coord_block_edge = [600, 10]
    coord_block_cloud = [1075, 10]

    dpg.set_item_pos("node_block_train", coord_block_train)
    dpg.set_item_pos("node_block_edge", coord_block_edge)
    dpg.set_item_pos("node_block_cloud", coord_block_cloud)

    dpg.set_item_pos("node_control", coord_module_interface)
    dpg.set_item_pos(object.object.edge_1.ID_node, coord_edge_1)
    dpg.set_item_pos(object.object.edge_2.ID_node, coord_edge_2)
    dpg.set_item_pos("node_capture", coord_module_capture)
    dpg.set_item_pos("node_train", coord_train)
    dpg.set_item_pos("node_slam", coord_component_process)
    dpg.set_item_pos("node_ai", coord_ai)
    dpg.set_item_pos("node_operator", coord_trainope)
    dpg.set_item_pos("node_ssd", coord_ssd)
    dpg.set_item_pos("node_data", coord_data)
    dpg.set_item_pos("node_network", coord_network)

    dpg.set_viewport_width(gui_width)
    dpg.set_viewport_height(gui_height)
    scheme_theme.scheme_theme_demo()
def update_node_pos_demo_fullscreen():
    gui_width = 1875
    gui_height = 1040
    coord_module_interface = [1175, 325]
    coord_module_capture = [290, 150]
    coord_edge_1 = [875, 525]
    coord_train = [50, 150]
    coord_component_process = [850, 350]
    coord_ai = [850, 550]
    coord_trainope = [1485, 250]
    coord_ssd = [1400, 325]
    coord_data = [800, 225]
    coord_legend = [1110, 10]
    coord_network = [150, 600]
    coord_block_train = [35, 50]
    coord_block_edge = [775, 125]
    coord_block_cloud = [1450, 50]

    dpg.set_item_pos("node_block_train", coord_block_train)
    dpg.set_item_pos("node_block_edge", coord_block_edge)
    dpg.set_item_pos("node_block_cloud", coord_block_cloud)

    dpg.set_item_pos("node_control", coord_module_interface)
    dpg.set_item_pos(object.object.edge_1.ID_node, coord_edge_1)
    dpg.set_item_pos("node_capture", coord_module_capture)
    dpg.set_item_pos("node_train", coord_train)
    dpg.set_item_pos("node_slam", coord_component_process)
    dpg.set_item_pos("node_ai", coord_ai)
    dpg.set_item_pos("node_operator", coord_trainope)
    dpg.set_item_pos("node_ssd", coord_ssd)
    dpg.set_item_pos("node_data", coord_data)
    dpg.set_item_pos("node_network", coord_network)

    dpg.set_viewport_width(gui_width)
    dpg.set_viewport_height(gui_height)
    scheme_theme.scheme_theme_demo()
def update_fullscreen(value):
    if(param_interface.gui_fullscreen == False and value == True):
        dpg.toggle_viewport_fullscreen()
        dpg.bind_item_font("window", param_interface.gui_font_big)
        dpg.set_item_width(object.object.capture.ID_wallet, 175)
        dpg.set_item_width(object.object.edge_1.ID_wallet, 175)
        dpg.set_item_width(object.object.edge_1.slam.ID_wallet, 175)
        dpg.set_item_width(object.object.edge_1.ai.ID_wallet, 175)
        dpg.set_item_width(object.object.operator.ID_wallet, 175)
        dpg.set_item_width(object.object.edge_1.ai.ID_setting_lidar_height, 150)
        dpg.set_item_width(object.object.edge_1.ai.ID_setting_threshold, 150)
        dpg.set_item_width(object.object.edge_1.ID_sock_client_l1_lidar_main, 120)
        dpg.set_item_width("legend_train", 30)
        dpg.set_item_width("legend_edge", 30)
        dpg.set_item_width("legend_cloud", 30)
        dpg.set_item_width("legend_control", 30)
        dpg.set_item_width(object.object.train.ID_l1_motor_speed, 125)
        param_interface.gui_fullscreen = True
    elif(param_interface.gui_fullscreen == True and value == False):
        dpg.toggle_viewport_fullscreen()
        dpg.bind_item_font("window", param_interface.gui_font_def)
        dpg.set_item_width(object.object.capture.ID_wallet, 120)
        dpg.set_item_width(object.object.edge_1.ID_wallet, 120)
        dpg.set_item_width(object.object.edge_1.slam.ID_wallet, 120)
        dpg.set_item_width(object.object.edge_1.ai.ID_wallet, 120)
        dpg.set_item_width(object.object.operator.ID_wallet, 120)
        dpg.set_item_width(object.object.edge_1.ai.ID_setting_lidar_height, 100)
        dpg.set_item_width(object.object.edge_1.ai.ID_setting_threshold, 100)
        dpg.set_item_width(object.object.edge_1.ID_sock_client_l1_lidar_main, 80)
        dpg.set_item_width("legend_train", 15)
        dpg.set_item_width("legend_edge", 15)
        dpg.set_item_width("legend_cloud", 15)
        dpg.set_item_width("legend_control", 15)
        dpg.set_item_width(object.object.train.ID_l1_motor_speed, 75)
        param_interface.gui_fullscreen = False
