#---------------------------------------------
from src.param import param_control
from src.gui.background import gui_ID
from src.element.base import window
from src.gui.style import gui_color
from src.utils import parser_json
import dearpygui.dearpygui as dpg


class Operator_window(window.Window):
    def build_parameter(self):
        with dpg.group(horizontal=True):
            dpg.add_text("Add:");
            dpg.add_combo(param_control.wallet_add, tag=self.ID.ID_wallet, label="", default_value=param_control.state_edge_1["cloud_operator"]["add"], width=120, callback=self.command_comboip)
        with dpg.group(horizontal=True):
            dpg.add_text("IP:");
            dpg.add_text("127.0.0.1", tag=self.ID.ID_ip, color=gui_color.color_info);

    def command_comboip(self):
        ip_operator = wallet_logic.get_ip_from_key(dpg.get_value(self.ID.ID_wallet))
        if(ip_operator != None):
            param_control.state_edge_1["cloud_operator"]["broker_ip"] = ip_operator
            dpg.set_value(self.ID.ID_ip, ip_operator)
            https_client_post.post_param_value("edge", "cloud_operator", "broker_ip", ip_operator)

    def save_coord_to_file(self):
        data = parser_json.get_pos_from_json()
        data["cloud"]["operator"] = dpg.get_item_pos(self.ID.ID_node)
        parser_json.upload_file(param_control.path_node_coordinate, data)
