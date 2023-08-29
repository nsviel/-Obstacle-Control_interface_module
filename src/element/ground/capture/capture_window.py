#---------------------------------------------
from src.param import param_control
from src.gui.background import gui_ID
from src.gui.style import gui_color
from src.element.misc.wallet import wallet_logic
from src.base import window
from src.utils import parser_json
from src.connection.HTTPS.client import https_client_post
from src.gui.style import colorization
import dearpygui.dearpygui as dpg


class Capture_window(window.Window):
    # Build function
    def build_parameter(self):
        with dpg.table(header_row=False, borders_innerH=True):
            dpg.add_table_column()
            dpg.add_table_column()
            with dpg.table_row():
                dpg.add_text("Address");
                dpg.add_combo(param_control.wallet_add, tag=self.ID.ID_wallet, label="", default_value="-", width=120, callback=self.command_new_add)
            with dpg.table_row():
                dpg.add_text("IP");
                dpg.add_text("127.0.0.1", tag=self.ID.ID_ip, color=gui_color.color_info);
            with dpg.table_row():
                dpg.add_text("Nb thread");
                dpg.add_text(1, tag=self.ID.ID_thread, color=gui_color.color_info);
        dpg.add_separator()
        self.colorize_window()
    def colorize_window(self):
        colorization.colorize_item(self.ID.ID_wallet, "node_sub")
        colorization.colorize_item(self.ID.ID_ip, "node_sub")

    # Command function
    def save_coord_to_file(self):
        pose = parser_json.get_pos_from_json()
        pose["ground"]["capture"] = dpg.get_item_pos(self.ID.ID_node)
        parser_json.upload_file(param_control.path_node_pose, pose)
    def command_new_add(self):
        add = dpg.get_value(self.ID.ID_wallet)
        ip = wallet_logic.get_ip_from_key(add)
        if(ip != None):
            dpg.set_value(self.ID.ID_ip, ip)
            param_control.state_ground["capture"]["info"]["ip"] = ip
            param_control.state_ground["capture"]["info"]["add"] = add
            https_client_post.post_state("ground", param_control.state_ground)

    # Update function
    def update(self):
        colorization.colorize_status(self.ID.ID_status, param_control.state_ground["capture"]["info"]["status"])
        dpg.set_value(self.ID.ID_status, param_control.state_ground["capture"]["info"]["status"])
        dpg.set_value(self.ID.ID_wallet, param_control.state_ground["capture"]["info"]["add"])
        dpg.set_value(self.ID.ID_ip, param_control.state_ground["capture"]["info"]["ip"])
        dpg.set_value(self.ID.ID_thread, param_control.state_ground["capture"]["info"]["nb_thread"])
