#---------------------------------------------
from src.param import param_control
from src.gui.background import gui_ID
from src.gui.style import gui_color
from src.element.base import window
from src.utils import parser_json
import dearpygui.dearpygui as dpg


class Control_window(window.Window):
    def build_parameter(self):
        with dpg.group(horizontal=True):
            dpg.add_text("IP:");
            dpg.add_text("127.0.0.1", tag=self.ID.ID_ip, color=gui_color.color_info);
        with dpg.group(horizontal=True):
            dpg.add_text("Nb thread:");
            dpg.add_text(1, tag=self.ID.ID_thread, color=gui_color.color_info);
        with dpg.group(horizontal=True):
            dpg.add_text("Temp:");
            dpg.add_text(0, tag=self.ID.ID_temperature, color=gui_color.color_info);
            dpg.add_text("°", color=gui_color.color_info);
        edges = ("France_1", "France_2", "Spain_1")
        dpg.add_combo(edges, tag=self.ID.ID_setting_edge_selection, label="Edge", default_value="France_1", width=125)

    def save_coord_to_file(self):
        data = parser_json.get_pos_from_json()
        data["cloud"]["control"] = dpg.get_item_pos(self.ID.ID_node)
        parser_json.upload_file(param_control.path_node_coordinate, data)
