#---------------------------------------------
from src.param import param_control
from src.base import window
from src.gui.style import gui_color
from src.utils import parser_json
from src.element.misc.wallet import wallet_logic
from src.connection.HTTPS.client import https_client_con
from src.connection.HTTPS.client import https_client_post
from src.gui.style import colorization
import dearpygui.dearpygui as dpg


class Hub_window(window.Window):
    # Build function
    def build_parameter(self):
        self.build_setting()
        dpg.add_separator()
        self.colorize_window()
        self.init_values()
    def build_setting(self):
        with dpg.table(header_row=False, borders_innerH=True):
            dpg.add_table_column()
            dpg.add_table_column()
            with dpg.table_row():
                dpg.add_text("IP");
                dpg.add_text("127.0.0.1", tag=self.ID.ID_ip, color=gui_color.color_info);
            with dpg.table_row():
                dpg.add_text("Address");
                dpg.add_combo(list(param_control.wallet.keys()), tag=self.ID.ID_wallet, label="", default_value="-", width=120, callback=self.command_new_add)
            with dpg.table_row():
                dpg.add_text("Nb thread");
                dpg.add_text(1, tag=self.ID.ID_thread, color=gui_color.color_info);
    def colorize_window(self):
        colorization.colorize_item(self.ID.ID_wallet, "node_sub")
        colorization.colorize_item(self.ID.ID_ip, "node_sub")
    def init_values(self):
        add = wallet_logic.get_add_from_ip(param_control.state_edge["hub"]["info"]["ip"])
        param_control.state_edge["hub"]["info"]["add"] = add
        dpg.set_value(self.ID.ID_wallet, add)

    # Command function
    def save_coord_to_file(self):
        pose = parser_json.get_pos_from_json()
        pose["edge"]["hub"] = dpg.get_item_pos(self.ID.ID_node)
        parser_json.upload_file(param_control.path_node_pose, pose)
    def command_new_add(self):
        add = dpg.get_value(self.ID.ID_wallet)
        ip = wallet_logic.get_ip_from_add(add)
        if(ip != None):
            dpg.set_value(self.ID.ID_ip, ip)
            param_control.state_edge["hub"]["info"]["ip"] = ip
            param_control.state_edge["hub"]["info"]["add"] = add
            https_client_con.test_connection_edge()
            https_client_post.post_state("edge", param_control.state_edge)

    # Update function
    def update(self):
        colorization.colorize_status(self.ID.ID_status, param_control.state_edge["hub"]["info"]["status"])
        dpg.configure_item(self.ID.ID_wallet, items=list(param_control.wallet.keys()))
        dpg.set_value(self.ID.ID_status, param_control.state_edge["hub"]["info"]["status"])
        dpg.set_value(self.ID.ID_edge_id, param_control.state_edge["hub"]["info"]["edge_id"])
        dpg.set_value(self.ID.ID_edge_country, param_control.state_edge["hub"]["info"]["country"])
        dpg.set_value(self.ID.ID_ip, param_control.state_edge["hub"]["info"]["ip"])
        dpg.set_value(self.ID.ID_thread, param_control.state_edge["hub"]["info"]["nb_thread"])
