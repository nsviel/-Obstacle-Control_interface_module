#---------------------------------------------
from src.param import param_control
from src.gui.background import gui_ID
from src.element.edge.network import network_command
from src.element.base import window
from src.utils import parser_json
import dearpygui.dearpygui as dpg


class Network_window(window.Window):
    def build_parameter(self):
        with dpg.table(tag=self.ID.ID_mongo_table, header_row=False, borders_innerH=True, width=350):
            dpg.add_table_column()
            dpg.add_table_column()

            with dpg.table_row():
                dpg.add_text("IP");
                dpg.add_input_text(tag=self.ID.ID_mongo_ip, label="", default_value="", width=150, on_enter=True, callback=network_command.callback_mongo_ip);
            with dpg.table_row():
                dpg.add_text("Port");
                dpg.add_input_int(tag=self.ID.ID_mongo_port, default_value=1, width=100, callback=network_command.callback_mongo_port);
            with dpg.table_row():
                dpg.add_text("Database");
                dpg.add_input_text(tag=self.ID.ID_mongo_db, label="", default_value="", width=150, on_enter=True, callback=network_command.callback_mongo_db);
            with dpg.table_row():
                dpg.add_text("Collection");
                dpg.add_input_text(tag=self.ID.ID_mongo_collection, label="", default_value="", width=150, on_enter=True, callback=network_command.callback_mongo_collection);
            with dpg.table_row():
                dpg.add_text("number of data");
                dpg.add_input_int(tag=self.ID.ID_mongo_nb_data, default_value=1, width=100, callback=network_command.callback_mongo_nbdata);
            with dpg.table_row():
                dpg.add_text("Username");
                dpg.add_input_text(tag=self.ID.ID_mongo_username, label="", default_value="", width=150, on_enter=True, callback=network_command.callback_mongo_username);
            with dpg.table_row():
                dpg.add_text("Password");
                dpg.add_input_text(tag=self.ID.ID_mongo_password, label="", default_value="", width=150, on_enter=True, callback=network_command.callback_mongo_password);

    def save_coord_to_file(self):
        data = parser_json.get_pos_from_json()
        data["edge"][self.ID.ID_edge]["network"] = dpg.get_item_pos(self.ID.ID_node)
        parser_json.upload_file(param_control.path_node_coordinate, data)
