#---------------------------------------------
from src.param import param_control
from src.gui.background import gui_ID
from src.base import window
from src.gui.style import colorization
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
                dpg.add_input_text(tag=self.ID.ID_mongo_ip, label="", default_value="", width=150, on_enter=True, callback=self.command_parameter);
            with dpg.table_row():
                dpg.add_text("Port");
                dpg.add_input_int(tag=self.ID.ID_mongo_port, default_value=1, width=100, callback=self.command_parameter);
            with dpg.table_row():
                dpg.add_text("Database");
                dpg.add_input_text(tag=self.ID.ID_mongo_db, label="", default_value="", width=150, on_enter=True, callback=self.command_parameter);
            with dpg.table_row():
                dpg.add_text("Collection");
                dpg.add_input_text(tag=self.ID.ID_mongo_collection, label="", default_value="", width=150, on_enter=True, callback=self.command_parameter);
            with dpg.table_row():
                dpg.add_text("number of data");
                dpg.add_input_int(tag=self.ID.ID_mongo_nb_data, default_value=1, width=100, callback=self.command_parameter);
            with dpg.table_row():
                dpg.add_text("Username");
                dpg.add_input_text(tag=self.ID.ID_mongo_username, label="", default_value="", width=150, on_enter=True, callback=self.command_parameter);
            with dpg.table_row():
                dpg.add_text("Password");
                dpg.add_input_text(tag=self.ID.ID_mongo_password, label="", default_value="", width=150, on_enter=True, callback=self.command_parameter);
        dpg.add_separator()
        self.colorize_window()
    def colorize_window(self):
        colorization.colorize_item(self.ID.ID_mongo_ip, "node_sub")
        colorization.colorize_item(self.ID.ID_mongo_port, "node_sub")
        colorization.colorize_item(self.ID.ID_mongo_db, "node_sub")
        colorization.colorize_item(self.ID.ID_mongo_collection, "node_sub")
        colorization.colorize_item(self.ID.ID_mongo_username, "node_sub")
        colorization.colorize_item(self.ID.ID_mongo_password, "node_sub")
        colorization.colorize_item(self.ID.ID_mongo_nb_data, "node_sub")

    # Command function
    def save_coord_to_file(self):
        pose = parser_json.get_pos_from_json()
        pose["edge"]["network"] = dpg.get_item_pos(self.ID.ID_node)
        parser_json.upload_file(param_control.path_node_pose, pose)
    def command_parameter():
        param_control.state_network["mongodb"]["ip"] = dpg.get_value(self.ID.ID_mongo_ip)
        param_control.state_network["mongodb"]["port"] = dpg.get_value(self.ID.ID_mongo_port)
        param_control.state_network["mongodb"]["database"] = dpg.get_value(self.ID.ID_mongo_db)
        param_control.state_network["mongodb"]["collection"] = dpg.get_value(self.ID.ID_mongo_collection)
        param_control.state_network["mongodb"]["username"] = dpg.get_value(self.ID.ID_mongo_username)
        param_control.state_network["mongodb"]["password"] = dpg.get_value(self.ID.ID_mongo_password)
        param_control.state_network["mongodb"]["nb_data"] = dpg.get_value(self.ID.ID_mongo_nb_data)
        https_client_post.post_state_edge("network", param_control.state_network)

    # Update function
    def update(self):
        dpg.set_value(self.ID.ID_mongo_ip, param_control.state_network["mongodb"]["ip"])
        dpg.set_value(self.ID.ID_mongo_port, param_control.state_network["mongodb"]["port"])
        dpg.set_value(self.ID.ID_mongo_db, param_control.state_network["mongodb"]["database"])
        dpg.set_value(self.ID.ID_mongo_collection, param_control.state_network["mongodb"]["collection"])
        dpg.set_value(self.ID.ID_mongo_username, param_control.state_network["mongodb"]["username"])
        dpg.set_value(self.ID.ID_mongo_password, param_control.state_network["mongodb"]["password"])
        dpg.set_value(self.ID.ID_mongo_nb_data, param_control.state_network["mongodb"]["nb_data"])
