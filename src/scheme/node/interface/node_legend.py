#---------------------------------------------
from src.scheme.style import scheme_function
from src.scheme.style import scheme_connection

import dearpygui.dearpygui as dpg


def design_node():
    with dpg.node(label="Legend", tag="node_legend"):
        scheme_function.add_legend_line("legend_train", "Train level components")
        scheme_function.add_legend_line("legend_edge", "Edge level components")
        scheme_function.add_legend_line("legend_cloud", "Cloud level components")
        scheme_function.add_legend_line("legend_control", "Control level components")
