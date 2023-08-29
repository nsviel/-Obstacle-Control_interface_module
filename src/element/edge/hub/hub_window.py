#---------------------------------------------
from src.param import param_control
from src.base import window
from src.gui.style import gui_color
from src.utils import parser_json
from src.element.misc.wallet import wallet_logic
from src.connection.HTTPS import https_client_con
from src.connection.HTTPS import https_client_post
from src.gui.style import colorization
import dearpygui.dearpygui as dpg


class Hub_window(window.Window):
    # Build function
    def build_parameter(self):
        with dpg.table(header_row=False, borders_innerH=True):
            dpg.add_table_column()
            dpg.add_table_column()
            with dpg.table_row():
                dpg.add_text("Address");
                dpg.add_combo(param_control.wallet_add, tag=self.ID.ID_wallet, label="", default_value="-", width=120, callback=self.command_comboip)
            with dpg.table_row():
                dpg.add_text("IP");
                dpg.add_text("127.0.0.1", tag=self.ID.ID_ip, color=gui_color.color_info);
            with dpg.table_row():
                dpg.add_text("Nb thread");
                dpg.add_text(1, tag=self.ID.ID_thread, color=gui_color.color_info);
        dpg.add_separator()
        #dpg.configure_item(self.ID.ID_wallet, items=param_control.wallet_add)

    # Command function
    def command_comboip(self):
        edge_ip = wallet_logic.get_ip_from_key(dpg.get_value(self.ID.ID_wallet))
        if(edge_ip != None):
            param_control.state_edge["hub"]["info"]["ip"] = edge_ip
            dpg.set_value(self.ID.ID_ip, edge_ip)
            https_client_con.test_connection_edge()
            https_client_post.post_state("edge", param_control.state_edge)
    def save_coord_to_file(self):
        pose = parser_json.get_pos_from_json()
        pose["edge"]["hub"] = dpg.get_item_pos(self.ID.ID_node)
        parser_json.upload_file(param_control.path_node_pose, pose)

    # Update function
    def update(self):
        pass
    def update_edge(self):
        if(edge.state["self"]["lidar_main"] == "lidar_1"):
            s1 = "lidar_1"
            s2 = "lidar_2"
        elif(edge.state["self"]["lidar_main"] == "lidar_2"):
            s1 = "lidar_2"
            s2 = "lidar_1"

        dpg.set_value(self.ID.ID_status, edge.state["self"]["status"])
        dpg.set_value(self.ID.ID_edge_id, edge.state["self"]["edge_id"])
        dpg.set_value(self.ID.ID_edge_country, edge.state["self"]["country"])
        dpg.set_value(self.ID.ID_wallet, edge.state["self"]["add"])
        dpg.set_value(self.ID.ID_ip, edge.state["self"]["ip"])
        dpg.set_value(self.ID.ID_thread, edge.state["self"]["nb_thread"])
        dpg.set_value(self.ID.ID_ip, edge.state["self"]["edge_id"])
        dpg.set_value(self.ID.ID_sock_server_l1_port, edge.state["self"]["sock_server_l1_port"])
        dpg.set_value(self.ID.ID_sock_server_l2_port, edge.state["self"]["sock_server_l2_port"])
        dpg.set_value(self.ID.ID_http_server_port, edge.state["self"]["http_server_port"])
        dpg.set_value(self.ID.ID_sock_client_l1_lidar_main, s1)
        dpg.set_value(self.ID.ID_sock_client_l2_source, s2)
        colorization.colorize_status_light(self.ID.ID_status_light, param_control.status_edge)
        colorization.colorize_item(self.ID.ID_wallet, "input_text")
        colorization.colorize_item(self.ID.ID_ip, "input_text")
