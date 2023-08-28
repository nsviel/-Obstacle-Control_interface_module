#---------------------------------------------
from src.param import param_control
from src.gui.background import gui_ID
from src.gui.style import gui_color
from src.element.misc.wallet import wallet_logic
from src.base import window
from src.utils import parser_json
from src.connection.HTTPS import https_client_post
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
                dpg.add_combo(param_control.wallet_add, tag=self.ID.ID_wallet, label="", default_value="-", width=120, callback=self.update_address)
            with dpg.table_row():
                dpg.add_text("IP");
                dpg.add_text("127.0.0.1", tag=self.ID.ID_ip, color=gui_color.color_info);
            with dpg.table_row():
                dpg.add_text("Nb thread");
                dpg.add_text(1, tag=self.ID.ID_thread, color=gui_color.color_info);
        dpg.add_separator()

    # Command function
    def save_coord_to_file(self):
        data = parser_json.get_pos_from_json()
        data["ground"]["capture"] = dpg.get_item_pos(self.ID.ID_node)
        parser_json.upload_file(param_control.path_node_coordinate, data)

    # Update function
    def update(self):
        pass
    def update_parameter(self):
        dpg.set_value(self.ID.ID_status, param_control.status_capture)
        dpg.set_value(self.ID.ID_wallet, param_control.state_edge["module_capture"]["add"])
        dpg.set_value(self.ID.ID_ip, param_control.state_edge["module_capture"]["ip"])
        dpg.set_value(self.ID.ID_thread, param_control.state_ground["self"]["nb_thread"])
        colorization.colorize_item(self.ID.ID_wallet, input_text)
        colorization.colorize_item(self.ID.ID_ip, input_text)
    def update_address(self):
        capture_ip = wallet_logic.get_ip_from_key(dpg.get_value(self.ID.ID_wallet))
        if(capture_ip != None):
            param_control.state_ground["self"]["ip"] = capture_ip
            dpg.set_value(self.ID.ID_ip, capture_ip)
            https_client_post.post_param_value("edge", "module_capture", "ip", capture_ip)
