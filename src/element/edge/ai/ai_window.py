#---------------------------------------------
from src.param import param_control
from src.gui.background import gui_ID
from src.base import window
from src.gui.style import gui_color
from src.connection.HTTPS import https_client_post
from src.utils import parser_json
from src.element.misc.wallet import wallet_logic
import dearpygui.dearpygui as dpg


class Ai_window(window.Window):
    # Build function
    def build_parameter(self):
        with dpg.table(header_row=False, borders_innerH=True):
            dpg.add_table_column()
            dpg.add_table_column()
            with dpg.table_row():
                dpg.add_text("Address");
                dpg.add_combo(param_control.wallet_add, tag=self.ID.ID_wallet, label="", default_value="localhost", width=120, callback=self.command_comboip)
            with dpg.table_row():
                dpg.add_text("IP");
                dpg.add_text("127.0.0.1", tag=self.ID.ID_ip, color=gui_color.color_info);
            with dpg.table_row():
                dpg.add_text("Height");
                dpg.add_input_float(tag=self.ID.ID_setting_lidar_height, default_value=2, width=100, step=0.1, min_value=0, callback=self.command_ai);
            with dpg.table_row():
                dpg.add_text("Threshold");
                dpg.add_input_float(tag=self.ID.ID_setting_threshold, default_value=0.2, width=100, step=0.01, min_value=0, max_value=1, callback=self.command_ai);
        dpg.add_separator()
    def colorize_window():
        #colorization.colorize_status(self.ID.ID_status_light, param_control.status_ai)
        colorization.colorize_item(self.ID.ID_setting_threshold, "input_text")
        colorization.colorize_item(self.ID.ID_setting_lidar_height, "input_text")

    # Command function
    def command_ai(self):
        param_control.state_edge["component"]["ai"]["parameter"]["lidar_height"] = dpg.get_value(self.ID.ID_setting_lidar_height)
        param_control.state_edge["component"]["ai"]["parameter"]["threshold"] = dpg.get_value(self.ID.ID_setting_threshold)
        https_client_post.post_state("edge", param_control.state_edge)
    def command_comboip(self):
        ai_ip = wallet_logic.get_ip_from_key(dpg.get_value(self.ID.ID_wallet))
        if(ai_ip != None):
            param_control.state_edge["component"]["ai"]["ip"] = ai_ip
            dpg.set_value(self.ID.ID_ip, ai_ip)
            https_client_post.post_state("edge", param_control.state_edge)
    def save_coord_to_file(self):
        data = parser_json.get_pos_from_json()
        data["edge"]["ai"] = dpg.get_item_pos(self.ID.ID_node)
        parser_json.upload_file(param_control.path_node_coordinate, data)

    # Update function
    def update(self):
        pass
    def update_ai(self):
        dpg.set_value(self.ID.ID_http_server_port, edge.state["ai"]["http_server_port"])
        dpg.set_value(self.ID.ID_status, param_control.status_ai)
