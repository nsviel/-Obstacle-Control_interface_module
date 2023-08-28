#---------------------------------------------
from src.param import param_control
from src.gui.background import gui_ID
from src.base import window
from src.gui.style import gui_color
from src.utils import parser_json
import dearpygui.dearpygui as dpg


class Slam_window(window.Window):
    def build_parameter(self):
        with dpg.table(header_row=False, borders_innerH=True):
            dpg.add_table_column()
            dpg.add_table_column()
            with dpg.table_row():
                dpg.add_text("Add:");
                dpg.add_combo(param_control.wallet_add, tag=self.ID.ID_wallet, label="", default_value="localhost", width=120, callback=self.command_comboip)
            with dpg.table_row():
                dpg.add_text("IP:");
                dpg.add_text("127.0.0.1", tag=self.ID.ID_ip, color=gui_color.color_info);
            with dpg.table_row():
                dpg.add_text("SLAM:");
                dpg.add_checkbox(tag=self.ID.ID_setting_with_slam, label="", default_value=True, callback=self.callback_component_process);
            with dpg.table_row():
                dpg.add_text("View:");
                dpg.add_radio_button(("Top", "Oblique"), tag=self.ID.ID_setting_cam_view, callback=self.callback_component_process, horizontal=True)
            with dpg.table_row():
                dpg.add_button(label="Reset", tag=self.ID.ID_setting_reset, width=50, callback=self.callback_component_process_reset)
        dpg.add_separator()

    def callback_component_process(self):
        https_client_post.post_param_value("ve", None, "slam", dpg.get_value(self.ID.ID_setting_with_slam))
        https_client_post.post_param_value("ve", None, "view", dpg.get_value(self.ID.ID_setting_cam_view))

    def callback_component_process_reset(self):
        https_client_post.post_param_value("ve", None, None, "reset")

    def command_comboip(self):
        processing_ip = wallet_logic.get_ip_from_key(dpg.get_value(self.ID.ID_wallet))
        if(processing_ip != None):
            param_control.state_edge["slam"]["ip"] = processing_ip
            dpg.set_value("edge_2_ip", processing_ip)
            https_client_post.post_param_value("edge", "slam", "ip", processing_ip)

    def update_slam(self):
        dpg.set_value(self.ID.ID_ip, edge.state["slam"]["ip"])
        dpg.set_value(self.ID.ID_sock_server_port, edge.state["slam"]["sock_server_port"])
        dpg.set_value(self.ID.ID_http_server_port, edge.state["slam"]["http_server_port"])
        dpg.set_value(self.ID.ID_status, param_control.status_processing)
        dpg.set_value(self.ID.ID_wallet, edge.state["slam"]["add"])

    def save_coord_to_file(self):
        data = parser_json.get_pos_from_json()
        data["edge"]["slam"] = dpg.get_item_pos(self.ID.ID_node)
        parser_json.upload_file(param_control.path_node_coordinate, data)
