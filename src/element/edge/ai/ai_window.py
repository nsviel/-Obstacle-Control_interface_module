#---------------------------------------------
from src.param import param_control
from src.gui.background import gui_ID
from src.element.base import window
from src.gui.style import gui_color
from src.connection.HTTPS import https_client_post
from src.utils import parser_json
import dearpygui.dearpygui as dpg


class Ai_window(window.Window):
    def build_parameter(self):
        with dpg.group(horizontal=True):
            dpg.add_text("Add:");
            dpg.add_combo(param_control.wallet_add, tag=self.ID.ID_wallet, label="", default_value="localhost", width=120, callback=self.command_comboip)
        with dpg.group(horizontal=True):
            dpg.add_text("IP:");
            dpg.add_text("127.0.0.1", tag=self.ID.ID_ip, color=gui_color.color_info);
        with dpg.group(horizontal=True):
            dpg.add_text("Height");
            dpg.add_input_float(tag=self.ID.ID_setting_lidar_height, default_value=2, width=100, step=0.1, min_value=0, callback=self.callback_ai);
        with dpg.group(horizontal=True):
            dpg.add_text("Threshold");
            dpg.add_input_float(tag=self.ID.ID_setting_threshold, default_value=0.2, width=100, step=0.01, min_value=0, max_value=1, callback=self.callback_ai);

    def callback_ai(self):
        https_client_post.post_param_value("component_ai", None, "lidar_height", dpg.get_value(self.ID.ID_setting_lidar_height))
        https_client_post.post_param_value("component_ai", None, "threshold", dpg.get_value(self.ID.ID_setting_threshold))

    def command_comboip(self):
        ai_ip = wallet_logic.get_ip_from_key(dpg.get_value(self.ID.ID_wallet))
        if(ai_ip != None):
            param_control.state_edge_1["component_ai"]["ip"] = ai_ip
            dpg.set_value(self.ID.ID_ip, ai_ip)
            https_client_post.post_param_value("edge", "component_ai", "ip", ai_ip)

    def update_ai(self):
        dpg.set_value(self.ID.ID_http_server_port, edge.state["component_ai"]["http_server_port"])
        dpg.set_value(self.ID.ID_status, param_control.status_ai)

    def save_coord_to_file(self):
        data = parser_json.get_pos_from_json()
        data["edge"]["ai"] = dpg.get_item_pos(self.ID.ID_node)
        parser_json.upload_file(param_control.path_node_coordinate, data)
