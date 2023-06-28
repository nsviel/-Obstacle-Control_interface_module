#---------------------------------------------
from src.scheme.style import scheme_color

import dearpygui.dearpygui as dpg


def scheme_theme_dev():
    color_white = (255, 255, 255)
    color_black = (0, 0, 0)
    color_node_grid_line = (75, 75, 75)
    color_node_grid_bkg = (75, 75, 75)
    color_node_bkg = (25, 25, 25)
    color_node_pin = (200, 200, 10)
    color_node_link = (255, 255, 255)
    link_thikness = 2

    with dpg.theme() as global_theme:
        with dpg.theme_component(dpg.mvAll):
            # Divers
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (20, 20, 20), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Text, color_white, category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Button, (100, 100, 100))
            dpg.add_theme_color(dpg.mvThemeCol_MenuBarBg, (0, 0, 0))

            # Plot
            dpg.add_theme_style(dpg.mvPlotStyleVar_LineWeight, 1, category=dpg.mvThemeCat_Plots)
            dpg.add_theme_style(dpg.mvPlotStyleVar_PlotPadding, x=0, y=0, category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_Line, color_white, category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_FrameBg, color_black, category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_PlotBg, color_black, category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_PlotBorder, color_black, category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_LegendBg, color_black, category=dpg.mvThemeCat_Plots)

            # Node background
            dpg.add_theme_color(dpg.mvNodeCol_NodeBackground, color_node_bkg, category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_NodeBackgroundHovered, color_node_bkg, category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_NodeBackgroundSelected, color_node_bkg, category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_NodeOutline, (0, 0, 0), category=dpg.mvThemeCat_Nodes)

            # Node link
            dpg.add_theme_color(dpg.mvNodeCol_Link, color_node_link, category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_LinkHovered, color_node_link, category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_LinkSelected, color_node_link, category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_style(dpg.mvNodeStyleVar_LinkThickness, link_thikness, category=dpg.mvThemeCat_Nodes)

            # Node
            dpg.add_theme_color(dpg.mvNodeCol_Pin, color_node_pin, category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_PinHovered, color_node_pin, category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_BoxSelector, (0, 0, 0, 100), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_BoxSelectorOutline, (175, 175, 175), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_style(dpg.mvNodeStyleVar_NodeCornerRounding, 1, category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_style(dpg.mvNodeStyleVar_NodePadding, x=8, y=4, category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_style(dpg.mvNodeStyleVar_PinQuadSideLength, 6, category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_style(dpg.mvNodeStyleVar_PinOffset, 4, category=dpg.mvThemeCat_Nodes)

            # Window
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, color_node_bkg, category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_TitleBg, color_node_bkg, category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, color_node_bkg, category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_TitleBgCollapsed, color_node_bkg, category=dpg.mvThemeCat_Core)

            # Minimap
            dpg.add_theme_color(dpg.mvNodesCol_MiniMapBackground, (0, 0, 0, 0), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodesCol_MiniMapOutline, (0, 0, 0, 0), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodesCol_MiniMapNodeBackground, (0, 0, 0, 0), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodesCol_MiniMapCanvas, (0, 0, 0, 0), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodesCol_MiniMapCanvasOutline, (0, 0, 0, 0), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodesCol_MiniMapNodeOutline, (0, 0, 0, 0), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodesCol_MiniMapLink, (0, 0, 0, 0), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodesCol_MiniMapNodeBackgroundHovered, (0, 0, 0, 0), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodesCol_MiniMapNodeBackgroundSelected, (0, 0, 0, 0), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodesCol_MiniMapLinkSelected, (0, 0, 0, 0), category=dpg.mvThemeCat_Nodes)

        # Background color
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvNodeCol_GridBackground, color_node_grid_bkg, category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_GridLine, color_node_grid_line, category=dpg.mvThemeCat_Nodes)

    dpg.bind_theme(global_theme)

def scheme_theme_demo():
    color_white = (255, 255, 255)
    color_black = (0, 0, 0)
    color_node_grid_line = (75, 75, 75)
    color_node_grid_bkg = (75, 75, 75)
    color_node_bkg = (25, 25, 25)
    color_node_pin = (200, 200, 10)
    color_node_link = (255, 255, 255)
    link_thikness = 2

    with dpg.theme() as global_theme:
        with dpg.theme_component(dpg.mvAll):
            # Divers
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (20, 20, 20), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Text, color_white, category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Button, (100, 100, 100))
            dpg.add_theme_color(dpg.mvThemeCol_MenuBarBg, (0, 0, 0))

            # Window
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, color_node_bkg, category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_TitleBg, color_node_bkg, category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, color_node_bkg, category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_TitleBgCollapsed, color_node_bkg, category=dpg.mvThemeCat_Core)

            # Plot
            dpg.add_theme_style(dpg.mvPlotStyleVar_LineWeight, 1, category=dpg.mvThemeCat_Plots)
            dpg.add_theme_style(dpg.mvPlotStyleVar_PlotPadding, x=0, y=0, category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_Line, color_white, category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_FrameBg, color_black, category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_PlotBg, color_black, category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_PlotBorder, color_black, category=dpg.mvThemeCat_Plots)
            dpg.add_theme_color(dpg.mvPlotCol_LegendBg, color_node_bkg, category=dpg.mvThemeCat_Plots)

            # Node background
            dpg.add_theme_color(dpg.mvNodeCol_NodeBackground, color_node_bkg, category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_NodeBackgroundHovered, color_node_bkg, category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_NodeBackgroundSelected, color_node_bkg, category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_NodeOutline, (0, 0, 0), category=dpg.mvThemeCat_Nodes)

            # Node
            dpg.add_theme_color(dpg.mvNodeCol_Pin, color_node_pin, category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_PinHovered, color_node_pin, category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_BoxSelector, (0, 0, 0, 100), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_BoxSelectorOutline, (175, 175, 175), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_style(dpg.mvNodeStyleVar_NodeCornerRounding, 1, category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_style(dpg.mvNodeStyleVar_NodePadding, x=8, y=4, category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_style(dpg.mvNodeStyleVar_PinQuadSideLength, 6, category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_style(dpg.mvNodeStyleVar_PinOffset, 4, category=dpg.mvThemeCat_Nodes)

            # Node link
            dpg.add_theme_color(dpg.mvNodeCol_Link, color_node_link, category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_LinkHovered, color_node_link, category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_LinkSelected, color_node_link, category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_style(dpg.mvNodeStyleVar_LinkThickness, link_thikness, category=dpg.mvThemeCat_Nodes)

            # Minimap
            dpg.add_theme_color(dpg.mvNodesCol_MiniMapBackground, (0, 0, 0, 0), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodesCol_MiniMapOutline, (0, 0, 0, 0), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodesCol_MiniMapNodeBackground, (0, 0, 0, 0), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodesCol_MiniMapCanvas, (0, 0, 0, 0), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodesCol_MiniMapCanvasOutline, (0, 0, 0, 0), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodesCol_MiniMapNodeOutline, (0, 0, 0, 0), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodesCol_MiniMapLink, (0, 0, 0, 0), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodesCol_MiniMapNodeBackgroundHovered, (0, 0, 0, 0), category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodesCol_MiniMapNodeBackgroundSelected, (0, 0, 0, 0), category=dpg.mvThemeCat_Nodes)

        # Background color
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvNodeCol_GridBackground, color_node_grid_bkg, category=dpg.mvThemeCat_Nodes)
            dpg.add_theme_color(dpg.mvNodeCol_GridLine, color_node_grid_line, category=dpg.mvThemeCat_Nodes)

    dpg.bind_theme(global_theme)

def colorize():
    colorize_node()
    colorize_item()

def colorize_node():
    # individual nodes
    layer_train = scheme_color.color_layer_train()
    layer_edge = scheme_color.color_layer_edge()
    layer_cloud = scheme_color.color_layer_cloud()
    layer_network = scheme_color.color_layer_network()

    dpg.bind_item_theme("node_co", layer_cloud)
    dpg.bind_item_theme("node_py", layer_train)
    dpg.bind_item_theme("node_train", layer_train)
    dpg.bind_item_theme("node_edge_1", layer_edge)
    dpg.bind_item_theme("node_ve", layer_edge)
    dpg.bind_item_theme("node_ai", layer_edge)
    dpg.bind_item_theme("node_data", layer_edge)
    dpg.bind_item_theme("node_edge_2", layer_cloud)
    dpg.bind_item_theme("node_operator", layer_cloud)
    dpg.bind_item_theme("node_cloud_car", layer_cloud)
    dpg.bind_item_theme("node_ssd", layer_cloud)
    dpg.bind_item_theme("node_network", layer_network)

    # Block
    block_train = scheme_color.color_block_train()
    block_edge = scheme_color.color_block_edge()
    block_cloud = scheme_color.color_block_cloud()

    dpg.bind_item_theme("node_block_train", block_train)
    dpg.bind_item_theme("node_block_edge", block_edge)
    dpg.bind_item_theme("node_block_cloud", block_cloud)

def colorize_legend():
    buton_train = scheme_color.color_buton_train()
    buton_edge = scheme_color.color_buton_edge()
    buton_cloud = scheme_color.color_buton_cloud()
    buton_control = scheme_color.color_buton_control()

    dpg.bind_item_theme("legend_train", buton_train)
    dpg.bind_item_theme("legend_edge", buton_edge)
    dpg.bind_item_theme("legend_cloud", buton_cloud)
    dpg.bind_item_theme("legend_control", buton_control)

def colorize_item():
    checkbox = scheme_color.color_checkbox()
    input_text = scheme_color.color_input_text()
    line_yaxis = scheme_color.color_yaxis_0()

    dpg.bind_item_theme("ssd_active", checkbox)
    dpg.bind_item_theme("l1_activated", checkbox)
    dpg.bind_item_theme("l2_activated", checkbox)
    dpg.bind_item_theme("processing_opt_slam", checkbox)

    dpg.bind_item_theme("ssd_path_add", input_text)
    dpg.bind_item_theme("ssd_path", input_text)
    dpg.bind_item_theme("trainope_mqtt_topic", input_text)
    dpg.bind_item_theme("l1_ip", input_text)
    dpg.bind_item_theme("l2_ip", input_text)
    dpg.bind_item_theme("l1_speed", input_text)
    dpg.bind_item_theme("l2_speed", input_text)
    dpg.bind_item_theme("ai_threshold", input_text)
    dpg.bind_item_theme("ai_lidar_height", input_text)

    dpg.bind_item_theme("interface_sock_server_l1_port", input_text)
    dpg.bind_item_theme("interface_sock_server_l2_port", input_text)
    dpg.bind_item_theme("capture_http_server_port", input_text)
    dpg.bind_item_theme("edge_sock_server_l1_port", input_text)
    dpg.bind_item_theme("edge_sock_server_l2_port", input_text)
    dpg.bind_item_theme("edge_mqtt_client_name", input_text)
    dpg.bind_item_theme("trainope_broker_port", input_text)
    dpg.bind_item_theme("edge_sock_client_l1_combo_lidar_main", input_text)
    dpg.bind_item_theme("processing_opt_view", input_text)
    dpg.bind_item_theme("l1_port", input_text)
    dpg.bind_item_theme("l2_port", input_text)

    dpg.bind_item_theme("edge_wallet", input_text)
    dpg.bind_item_theme("capture_wallet", input_text)
    dpg.bind_item_theme("edgenext_wallet", input_text)
    dpg.bind_item_theme("processing_wallet", input_text)
    dpg.bind_item_theme("ai_wallet", input_text)
    dpg.bind_item_theme("trainope_wallet", input_text)
    dpg.bind_item_theme("l1_wallet", input_text)
    dpg.bind_item_theme("l2_wallet", input_text)

    dpg.bind_item_theme("capture_ip", input_text)
    dpg.bind_item_theme("edge_ip", input_text)
    dpg.bind_item_theme("edgenext_ip", input_text)
    dpg.bind_item_theme("ai_ip", input_text)
    dpg.bind_item_theme("processing_ip", input_text)
    dpg.bind_item_theme("ip_operator", input_text)

    dpg.bind_item_theme("mongo_ip", input_text)
    dpg.bind_item_theme("mongo_port", input_text)
    dpg.bind_item_theme("mongo_db", input_text)
    dpg.bind_item_theme("mongo_collection", input_text)
    dpg.bind_item_theme("mongo_username", input_text)
    dpg.bind_item_theme("mongo_password", input_text)
    dpg.bind_item_theme("mongo_nbdata", input_text)

    dpg.bind_item_theme("l1_yaxis_line", line_yaxis)
    dpg.bind_item_theme("l2_yaxis_line", line_yaxis)

def colorize_status(tag, value, on, off):
    if(value == "Online" or value == True):
        dpg.bind_item_theme(tag, on)
    elif(value == "Offline" or value == False):
        dpg.bind_item_theme(tag, off)

def colorize_onoff(tag_on, tag_off, state):
    color_on = scheme_color.color_buton_green()
    color_off = scheme_color.color_buton_red()
    color_grey = scheme_color.color_buton_gray()
    if(state == True):
        dpg.bind_item_theme(tag_on, color_on)
        dpg.bind_item_theme(tag_off, color_grey)
    elif(state == False):
        dpg.bind_item_theme(tag_on, color_grey)
        dpg.bind_item_theme(tag_off, color_off)
