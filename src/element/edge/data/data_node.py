#---------------------------------------------
from src.param import param_control
from src.base import node
from src.gui.style import colorization
from src.gui.style import gui_color
from src.utils import parser_json
import dearpygui.dearpygui as dpg


class Data_node(node.Node):
    def build(self):
        self.ID.init_ID_icon()
        with dpg.node(label=self.ID.name, tag=self.ID.ID_node):
            with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
                dpg.add_image(self.ID.ID_icon_image, width=300, height=150)
            self.build_plot("lidar 1", self.ID.ID_yaxis_l1, self.ID.ID_plot_l1)
            self.build_plot("lidar 2", self.ID.ID_yaxis_l2, self.ID.ID_plot_l2)
            with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
                with dpg.group(horizontal=True):
                    dpg.add_text("Frame:");
                    dpg.add_text(0, tag=self.ID.ID_nb_frame, color=gui_color.color_node_value);
                with dpg.group(horizontal=True):
                    dpg.add_text("Prediction:");
                    dpg.add_text(0, tag=self.ID.ID_nb_prediction, color=gui_color.color_node_value);
        self.position_node()

    def build_plot(self, label, tag_y, tag_plot):
        x = []
        y = []
        for i in range(0, param_control.nb_tic):
            x.append(i)
            y.append(0)
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.plot(no_menus=True, no_box_select=True, no_mouse_pos=True, height=50, width=300):
                dpg.add_plot_legend()
                dpg.add_plot_axis(dpg.mvXAxis, no_gridlines=True, no_tick_marks=True, no_tick_labels=True)
                dpg.add_plot_axis(dpg.mvYAxis, no_tick_labels=True, no_gridlines=True, no_tick_marks=True, tag=tag_y)
                dpg.add_plot_axis(dpg.mvYAxis, no_tick_labels=True, no_gridlines=True, no_tick_marks=True, tag=tag_y+"_0")
                dpg.set_axis_limits(tag_y, -50, 1500)
                dpg.set_axis_limits(tag_y+"_0", -50, 1500)
                dpg.add_line_series(x, y, parent=tag_y+"_0", tag=tag_y+"_line")
                dpg.add_line_series(x, y, label=label, parent=tag_y, tag=tag_plot)

    def position_node(self):
        data = parser_json.get_pos_from_json()
        dpg.set_item_pos(self.ID.ID_node, data["edge"]["data"])

    def update_node(self):
        colorization.colorize_status("mongo_server_but", param_control.status_db)

    def update_perf():
        # Throughput
        value = "%.2f"% param_control.state_ground[param_control.lidar_main]["throughput"]["value"]
        dpg.set_value("perf_throughput_up_val", value)

        # Latency
        value = "%.2f"% param_control.state_network["local_cloud"]["latency"]["value"]
        dpg.set_value("perf_latency_up_val", value)
        value = "%.2f"% param_control.state_network["cloud_local"]["latency"]["value"]
        dpg.set_value("perf_latency_do_val", value)

        # Reliability
        value = "%.2f"% param_control.state_network["local_cloud"]["reliability"]["value"]
        dpg.set_value("perf_reliability_up_val", value)
        value = "%.2f"% param_control.state_network["cloud_local"]["reliability"]["value"]
        dpg.set_value("perf_reliability_do_val", value)

        # Interruption time
        value = "%.2f"% param_control.state_network["local_cloud"]["interruption"]["value"]
        dpg.set_value("perf_interruption_val", value)

        # End to end time
        dpg.set_value("perf_time_total", param_control.state_network["end_to_end"]["time_total"])
