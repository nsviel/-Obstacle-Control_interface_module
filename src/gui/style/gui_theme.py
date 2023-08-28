#---------------------------------------------
from src.param import param_control
import dearpygui.dearpygui as dpg

color_info = (0, 200, 200)
color_title = (200, 200, 200)


def gui_font():
    with dpg.font_registry():
        param_control.gui_font_def = dpg.add_font("src/gui/font/ProggyClean.ttf", 13)
        param_control.gui_font_big = dpg.add_font("src/gui/font/DroidSans.ttf", 25)

def gui_theme():
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
            dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, x=4, y=4, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, 0, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, x=4, y=4, category=dpg.mvThemeCat_Core)

            # Divers
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (20, 20, 20), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Text, color_white, category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Button, (100, 100, 100))
            dpg.add_theme_color(dpg.mvThemeCol_MenuBarBg, (0, 0, 0))

            # Window
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (75, 75, 75), category=dpg.mvThemeCat_Core)
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
            dpg.add_theme_style(dpg.mvNodeStyleVar_LinkLineSegmentsPerLength, 1, category=dpg.mvThemeCat_Nodes)
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
