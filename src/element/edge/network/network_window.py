#---------------------------------------------
from src.param import param_control
from src.gui.background import gui_ID
from src.element.edge.network import network_command
from src.base import window
from src.utils import parser_json
import dearpygui.dearpygui as dpg


class Network_window(window.Window):
    # Build function
    def build_parameter(self):
        dpg.add_text("MongoDB", color=(150, 150, 150));
        with dpg.table(tag=self.ID.ID_mongo_table, header_row=False, borders_innerH=True):
            dpg.add_table_column()
            dpg.add_table_column()

            with dpg.table_row():
                dpg.add_text("IP");
                dpg.add_input_text(tag=self.ID.ID_mongo_ip, label="", default_value="", width=150, on_enter=True, callback=network_command.callback_mongodb_state);
            with dpg.table_row():
                dpg.add_text("Port");
                dpg.add_input_int(tag=self.ID.ID_mongo_port, default_value=1, width=100, callback=network_command.callback_mongodb_state);
            with dpg.table_row():
                dpg.add_text("Database");
                dpg.add_input_text(tag=self.ID.ID_mongo_db, label="", default_value="", width=150, on_enter=True, callback=network_command.callback_mongodb_state);
            with dpg.table_row():
                dpg.add_text("Collection");
                dpg.add_input_text(tag=self.ID.ID_mongo_collection, label="", default_value="", width=150, on_enter=True, callback=network_command.callback_mongodb_state);
            with dpg.table_row():
                dpg.add_text("number of data");
                dpg.add_input_int(tag=self.ID.ID_mongo_nb_data, default_value=1, width=100, callback=network_command.callback_mongodb_state);
            with dpg.table_row():
                dpg.add_text("Username");
                dpg.add_input_text(tag=self.ID.ID_mongo_username, label="", default_value="", width=150, on_enter=True, callback=network_command.callback_mongodb_state);
            with dpg.table_row():
                dpg.add_text("Password");
                dpg.add_input_text(tag=self.ID.ID_mongo_password, label="", default_value="", width=150, on_enter=True, callback=network_command.callback_mongodb_state);
        dpg.add_separator()

    # Command function
    def save_coord_to_file(self):
        pose = parser_json.get_pos_from_json()
        pose["edge"]["network"] = dpg.get_item_pos(self.ID.ID_node)
        parser_json.upload_file(param_control.path_node_pose, pose)

    # Update function
    def update(self):
        pass
    def colorize_node(self):
        colorization.colorize_item(self.ID.ID_mongo_ip, input_text)
        colorization.colorize_item(self.ID.ID_mongo_port, input_text)
        colorization.colorize_item(self.ID.ID_mongo_db, input_text)
        colorization.colorize_item(self.ID.ID_mongo_collection, input_text)
        colorization.colorize_item(self.ID.ID_mongo_username, input_text)
        colorization.colorize_item(self.ID.ID_mongo_password, input_text)
        colorization.colorize_item(self.ID.ID_mongo_nb_data, input_text)
