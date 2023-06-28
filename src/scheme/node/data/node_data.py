#---------------------------------------------
from src.scheme.style import scheme_function
from src.scheme.style import scheme_connection

import dearpygui.dearpygui as dpg


def design_node():
    with dpg.node(label="Processed data", tag="node_data"):
        scheme_function.add_image_sized("image_in", 300, 150)

        scheme_function.add_plot("lidar 1", "l1_yaxis", "l1_plot", "l1_plot_visible")
        scheme_function.add_plot("lidar 2", "l2_yaxis", "l2_plot", "l2_plot_visible")
        scheme_function.add_variable_simple("Frame:", "nb_frame")
        scheme_function.add_variable_simple("Prediction:", "nb_prediction")
