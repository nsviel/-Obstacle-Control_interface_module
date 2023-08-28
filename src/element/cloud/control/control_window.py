#---------------------------------------------
from src.param import param_control
from src.gui.background import gui_ID
from src.gui.style import gui_color
from src.base import window
from src.utils import parser_json
from src.gui.style import colorization
import dearpygui.dearpygui as dpg


class Control_window(window.Window):
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

    def save_coord_to_file(self):
        data = parser_json.get_pos_from_json()
        data["cloud"]["control"] = dpg.get_item_pos(self.ID.ID_node)
        parser_json.upload_file(param_control.path_node_coordinate, data)

    def colorize_window():
        colorization.colorize_status(self.ID.ID_status_light, param_control.status_control)
