#---------------------------------------------
from src.param import param_control
from src.element.base import window
from src.gui.style import gui_color
from src.utils import parser_json
import dearpygui.dearpygui as dpg


class Hub_window(window.Window):
    def build_parameter(self):
        with dpg.group(horizontal=True):
            dpg.add_text("Add:");
            dpg.add_combo(param_control.wallet_add, tag=self.ID.ID_wallet, label="", default_value="-", width=120, callback=self.command_comboip)
        with dpg.group(horizontal=True):
            dpg.add_text("IP:");
            dpg.add_text("127.0.0.1", tag=self.ID.ID_ip, color=gui_color.color_info);
        with dpg.group(horizontal=True):
            dpg.add_text("Nb thread:");
            dpg.add_text(1, tag=self.ID.ID_thread, color=gui_color.color_info);

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

    def command_comboip(self):
        edge_ip = wallet_logic.get_ip_from_key(dpg.get_value(self.ID.ID_wallet))
        if(edge_ip != None):
            param_control.state_control["edge"]["ip"] = edge_1_ip
            dpg.set_value(self.ID.ID_ip, edge_1_ip)
            https_client_con.test_http_edge()
            https_client_post.post_param_value("capture", "edge_1", "ip", edge_1_ip)

    def save_coord_to_file(self):
        data = parser_json.get_pos_from_json()
        data["edge"]["hub"] = dpg.get_item_pos(self.ID.ID_node)
        parser_json.upload_file(param_control.path_node_coordinate, data)
