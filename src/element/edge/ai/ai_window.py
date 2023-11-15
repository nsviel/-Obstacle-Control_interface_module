#---------------------------------------------
from src.param import param_control
from src.gui.background import gui_ID
from src.base import window
from src.gui.style import gui_color
from src.gui.style import colorization
from src.connection.HTTPS.client import https_client_post
from src.utils import parser_json
import dearpygui.dearpygui as dpg


class Ai_window(window.Window):
    # Build function
    def build_parameter(self):
        with dpg.table(header_row=False, borders_innerH=True):
            dpg.add_table_column()
            dpg.add_table_column()
            with dpg.table_row():
                dpg.add_text("Height");
                dpg.add_input_float(tag=self.ID.ID_setting_lidar_height, default_value=2, width=100, step=0.1, min_value=0, callback=self.command_parameter);
            with dpg.table_row():
                dpg.add_text("Threshold");
                dpg.add_input_float(tag=self.ID.ID_setting_threshold, default_value=0.2, width=100, step=0.01, min_value=0, max_value=1, callback=self.command_parameter);
        dpg.add_separator()
        self.colorize_window()
        self.init_values()
    def colorize_window(self):
        colorization.colorize_item(self.ID.ID_setting_threshold, "node_sub")
        colorization.colorize_item(self.ID.ID_setting_lidar_height, "node_sub")
    def init_values(self):
        dpg.set_value(self.ID.ID_setting_lidar_height, param_control.state_edge["ai"]["parameter"]["lidar_height"])
        dpg.set_value(self.ID.ID_setting_threshold, param_control.state_edge["ai"]["parameter"]["threshold"])

    # Command function
    def command_parameter(self):
        param_control.state_edge["ai"]["parameter"]["lidar_height"] = dpg.get_value(self.ID.ID_setting_lidar_height)
        param_control.state_edge["ai"]["parameter"]["threshold"] = dpg.get_value(self.ID.ID_setting_threshold)
        https_client_post.post_state_edge("edge", param_control.state_edge)
    def save_coord_to_file(self):
        pose = parser_json.get_pos_from_json()
        pose["edge"]["ai"] = dpg.get_item_pos(self.ID.ID_node)
        parser_json.upload_file(param_control.path_node_pose, pose)

    # Update function
    def update(self):
        colorization.colorize_status(self.ID.ID_status, param_control.state_edge["ai"]["info"]["status"])
        dpg.set_value(self.ID.ID_status, param_control.state_edge["ai"]["info"]["status"])
