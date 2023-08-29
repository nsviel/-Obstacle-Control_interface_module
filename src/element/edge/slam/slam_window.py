#---------------------------------------------
from src.param import param_control
from src.gui.background import gui_ID
from src.base import window
from src.gui.style import gui_color
from src.utils import parser_json
from src.gui.style import colorization
from src.element.misc.wallet import wallet_logic
from src.connection.HTTPS import https_client_post
import dearpygui.dearpygui as dpg


class Slam_window(window.Window):
    # Build function
    def build_parameter(self):
        with dpg.table(header_row=False, borders_innerH=True):
            dpg.add_table_column()
            dpg.add_table_column()
            with dpg.table_row():
                dpg.add_text("Activated");
                dpg.add_checkbox(tag=self.ID.ID_setting_with_slam, label="", default_value=True, callback=self.command_component_process);
            with dpg.table_row():
                dpg.add_text("View");
                dpg.add_radio_button(("Top", "Oblique"), tag=self.ID.ID_setting_cam_view, callback=self.command_component_process, horizontal=True)
            with dpg.table_row():
                dpg.add_button(label="Reset", tag=self.ID.ID_setting_reset, width=50, callback=self.command_component_process_reset)
        dpg.add_separator()
        #colorization.colorize_status_light(self.ID.ID_status_light, param_control.state_edge["slam"]["info"]["status"])

    # Command function
    def command_component_process(self):
        param_control.state_edge["slam"]["parameter"]["with_slam"] = dpg.get_value(self.ID.ID_setting_with_slam)
        param_control.state_edge["slam"]["parameter"]["cam_view"] = dpg.get_value(self.ID.ID_setting_cam_view)
        https_client_post.post_state("edge", param_control.state_edge)
    def command_component_process_reset(self):
        https_client_post.post_commande("edge", "slam", "reset")
    def save_coord_to_file(self):
        pose = parser_json.get_pos_from_json()
        pose["edge"]["slam"] = dpg.get_item_pos(self.ID.ID_node)
        parser_json.upload_file(param_control.path_node_pose, pose)

    # Update function
    def update(self):
        pass
    def update_slam(self):
        dpg.set_value(self.ID.ID_ip, edge.state["slam"]["ip"])
        dpg.set_value(self.ID.ID_sock_server_port, edge.state["slam"]["sock_server_port"])
        dpg.set_value(self.ID.ID_http_server_port, edge.state["slam"]["http_server_port"])
        dpg.set_value(self.ID.ID_status, param_control.state_edge["slam"]["info"]["status"])
        dpg.set_value(self.ID.ID_wallet, edge.state["slam"]["add"])
