#---------------------------------------------
from src.param import param_control
from src.gui.background import gui_ID
from src.gui.style import gui_color
from src.base import window
from src.utils import parser_json
from src.gui.style import colorization
import dearpygui.dearpygui as dpg


class Control_window(window.Window):
    # Build function
    def build_parameter(self):
        with dpg.table(header_row=False, borders_innerH=True):
            dpg.add_table_column()
            dpg.add_table_column()
            with dpg.table_row():
                dpg.add_text("IP");
                dpg.add_text("127.0.0.1", tag=self.ID.ID_ip, color=gui_color.color_info);
            with dpg.table_row():
                dpg.add_text("Nb thread");
                dpg.add_text(1, tag=self.ID.ID_thread, color=gui_color.color_info);
            with dpg.table_row():
                dpg.add_text("Temperature");
                with dpg.group(horizontal=True):
                    dpg.add_text(0, tag=self.ID.ID_temperature, color=gui_color.color_info);
                    dpg.add_text("°", color=gui_color.color_info);
            edges = ("France_1", "France_2", "Spain_1")
            with dpg.table_row():
                dpg.add_text("Edge");
                dpg.add_combo(edges, tag=self.ID.ID_setting_edge_selection, default_value="France_1", width=125)
        dpg.add_separator()
    def colorize_window():
        colorization.colorize_status(self.ID.ID_status_light, param_control.state_control["control"]["info"]["status"])

    # Command function
    def save_coord_to_file(self):
        pose = parser_json.get_pos_from_json()
        pose["cloud"]["control"] = dpg.get_item_pos(self.ID.ID_node)
        parser_json.upload_file(param_control.path_node_pose, pose)

    # Update function
    def update(self):
        pass
    def update_node(self):
        dpg.set_value(self.ID.ID_status, param_control.state_control["control"]["info"]["status"])
        dpg.set_value(self.ID.ID_ip, param_control.state_control["control"]["ip"])
        dpg.set_value(self.ID.ID_thread, param_control.state_control["control"]["nb_thread"])
        dpg.set_value(self.ID.ID_temperature, signal.get_temps_core(0))
