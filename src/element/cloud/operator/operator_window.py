#---------------------------------------------
from src.param import param_control
from src.gui.background import gui_ID
from src.base import window
from src.gui.style import gui_color
from src.utils import parser_json
from src.element.misc.wallet import wallet_logic
from src.connection.HTTPS import https_client_post
from src.gui.style import colorization
import dearpygui.dearpygui as dpg


class Operator_window(window.Window):
    # Build function
    def build_parameter(self):
        with dpg.table(header_row=False, borders_innerH=True):
            dpg.add_table_column()
            dpg.add_table_column()
            with dpg.table_row():
                dpg.add_text("Address");
                dpg.add_combo(param_control.wallet_add, tag=self.ID.ID_wallet, label="", default_value=param_control.state_edge["interface"]["operator"]["add"], width=120, callback=self.command_comboip)
            with dpg.table_row():
                dpg.add_text("IP");
                dpg.add_text("127.0.0.1", tag=self.ID.ID_ip, color=gui_color.color_info);
        dpg.add_separator()
    def colorize_window():
        colorization.colorize_status(self.ID.ID_status_light, param_control.status_operator)
        colorization.colorize_item(self.ID.ID_wallet, input_text)
        colorization.colorize_item(self.ID.ID_ip, input_text)

    # Command function
    def command_comboip(self):
        ip_operator = wallet_logic.get_ip_from_key(dpg.get_value(self.ID.ID_wallet))
        if(ip_operator != None):
            param_control.state_edge["interface"]["operator"]["broker_ip"] = ip_operator
            dpg.set_value(self.ID.ID_ip, ip_operator)
            https_client_post.post_state("edge", param_control.state_edge)
    def save_coord_to_file(self):
        data = parser_json.get_pos_from_json()
        data["cloud"]["operator"] = dpg.get_item_pos(self.ID.ID_node)
        parser_json.upload_file(param_control.path_node_coordinate, data)

    # Update function
    def update(self):
        pass
