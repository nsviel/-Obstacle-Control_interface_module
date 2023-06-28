#---------------------------------------------
from src.param import param_interface
from src.scheme.style import scheme_theme

import dearpygui.dearpygui as dpg


def update_node_pos_dev():
    gui_width = param_interface.state_interface["gui"]["width"]
    gui_height = param_interface.state_interface["gui"]["height"]
    coord_module_interface = [1100, 600]
    coord_module_capture = [250, 10]
    coord_edge_1 = [725, 400]
    coord_train = [10, 10]
    coord_edge_next = [1150, 215]
    coord_component_process = [400, 510]
    coord_ai = [400, 745]
    coord_trainope = [1150, 50]
    coord_cloud_car = [1150, 450]
    coord_ssd = [1325, 600]
    coord_data = [650, 10]
    coord_network = [10, 510]

    dpg.set_item_pos("node_co", coord_module_interface)
    dpg.set_item_pos("node_edge_1", coord_edge_1)
    dpg.set_item_pos("node_py", coord_module_capture)
    dpg.set_item_pos("node_train", coord_train)
    dpg.set_item_pos("node_edge_2", coord_edge_next)
    dpg.set_item_pos("node_ve", coord_component_process)
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
    gui_height = 750
    coord_module_interface = [1175, 325]
    coord_module_capture = [290, 100]
    coord_edge_1 = [675, 100]
    coord_edge_2 = [675, 350]
    coord_train = [25, 100]
    coord_component_process = [850, 350]
    coord_ai = [850, 550]
    coord_trainope = [1110, 250]
    coord_ssd = [1400, 325]
    coord_data = [1000, 400]
    coord_legend = [1110, 10]
    coord_network = [75, 400]
    coord_block_train = [10, 10]
    coord_block_edge = [550, 10]
    coord_block_cloud = [1075, 10]

    dpg.set_item_pos("node_block_train", coord_block_train)
    dpg.set_item_pos("node_block_edge", coord_block_edge)
    dpg.set_item_pos("node_block_cloud", coord_block_cloud)

    dpg.set_item_pos("node_co", coord_module_interface)
    dpg.set_item_pos("node_edge_1", coord_edge_1)
    dpg.set_item_pos("node_edge_2", coord_edge_2)
    dpg.set_item_pos("node_py", coord_module_capture)
    dpg.set_item_pos("node_train", coord_train)
    dpg.set_item_pos("node_ve", coord_component_process)
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

    dpg.set_item_pos("node_co", coord_module_interface)
    dpg.set_item_pos("node_edge_1", coord_edge_1)
    dpg.set_item_pos("node_py", coord_module_capture)
    dpg.set_item_pos("node_train", coord_train)
    dpg.set_item_pos("node_ve", coord_component_process)
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
        dpg.set_item_width("capture_wallet", 175)
        dpg.set_item_width("edge_1_wallet", 175)
        dpg.set_item_width("processing_wallet", 175)
        dpg.set_item_width("ai_wallet", 175)
        dpg.set_item_width("trainope_wallet", 175)
        dpg.set_item_width("ai_lidar_height", 150)
        dpg.set_item_width("ai_threshold", 150)
        dpg.set_item_width("edge_1_sock_client_l1_combo_lidar_main", 120)
        dpg.set_item_width("legend_train", 30)
        dpg.set_item_width("legend_edge", 30)
        dpg.set_item_width("legend_cloud", 30)
        dpg.set_item_width("legend_control", 30)
        dpg.set_item_width("l1_speed", 125)
        param_interface.gui_fullscreen = True
    elif(param_interface.gui_fullscreen == True and value == False):
        dpg.toggle_viewport_fullscreen()
        dpg.bind_item_font("window", param_interface.gui_font_def)
        dpg.set_item_width("capture_wallet", 120)
        dpg.set_item_width("edge_1_wallet", 120)
        dpg.set_item_width("processing_wallet", 120)
        dpg.set_item_width("ai_wallet", 120)
        dpg.set_item_width("trainope_wallet", 120)
        dpg.set_item_width("ai_lidar_height", 100)
        dpg.set_item_width("ai_threshold", 100)
        dpg.set_item_width("edge_1_sock_client_l1_combo_lidar_main", 80)
        dpg.set_item_width("legend_train", 15)
        dpg.set_item_width("legend_edge", 15)
        dpg.set_item_width("legend_cloud", 15)
        dpg.set_item_width("legend_control", 15)
        dpg.set_item_width("l1_speed", 75)
        param_interface.gui_fullscreen = False
