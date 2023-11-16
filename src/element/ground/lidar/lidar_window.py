#---------------------------------------------
from src.param import param_control
from src.base import window
from src.gui.background import gui_ID
from src.element import element
from src.gui.style import gui_color
from src.utils import parser_json
from src.utils import io
from src.connection.HTTPS.client import https_client_post
from src.gui.style import colorization
import dearpygui.dearpygui as dpg


class Lidar_window(window.Window):
    # Build function
    def build_parameter(self):
        self.build_setting()
        self.build_stats()
        self.build_device()
        dpg.add_separator()
        self.colorize_window()
        self.init_values()
    def build_setting(self):
        with dpg.table(header_row=False, borders_innerH=True):
            dpg.add_table_column()
            dpg.add_table_column()
            with dpg.table_row():
                with dpg.group(horizontal=True):
                    dpg.add_text("Activated", color=gui_color.color_title);
                    dpg.add_checkbox(tag=self.ID.ID_activated, label="", default_value=True, indent=75, callback=self.command_parameter);
                with dpg.group(horizontal=True):
                    dpg.add_button(label="ON ", tag=self.ID.ID_motor_on, width=50, callback=self.command_motor_start)
                    dpg.add_button(label="OFF", tag=self.ID.ID_motor_off, width=50, callback=self.command_motor_stop)
            with dpg.table_row():
                dpg.add_text("IP");
                dpg.add_input_text(tag=self.ID.ID_ip, label="", default_value="", width=150, on_enter=True, callback=self.command_parameter);
            with dpg.table_row():
                dpg.add_text("Address");
                dpg.add_combo(element.object.misc.wallet.logic.get_list_add(), tag=self.ID.ID_wallet, label="", default_value="-", width=120, callback=self.command_new_add)
            with dpg.table_row():
                dpg.add_text("Speed");
                with dpg.group(horizontal=True):
                    dpg.add_input_int(tag=self.ID.ID_motor_speed, default_value=600, step=60, min_value=0, max_value=1200, width=75, min_clamped=True, max_clamped=True, callback=self.command_motor_speed);
                    dpg.add_text("rpm");
    def build_stats(self):
        with dpg.table(header_row=False, borders_innerH=True):
            dpg.add_table_column()
            dpg.add_table_column()
            with dpg.table_row():
                dpg.add_text("Packet");
                dpg.add_text(0, tag=self.ID.ID_stat_packet, color=gui_color.color_info);
            with dpg.table_row():
                dpg.add_text("Throughput");
                with dpg.group(horizontal=True):
                    dpg.add_text(0, tag=self.ID.ID_throughtput_value, color=gui_color.color_info);
                    dpg.add_text("Mb/s");
        with dpg.group(horizontal=True):
            dpg.add_text("[");
            dpg.add_text(0, tag=self.ID.ID_throughtput_range, color=gui_color.color_info);
            dpg.add_text("]");
            dpg.add_text("Mb/s");
    def build_device(self):
        dpg.add_text("Device")
        dpg.add_listbox(tag=self.ID.ID_device_list, callback=self.command_parameter, width=250)
    def colorize_window(self):
        colorization.colorize_item(self.ID.ID_activated, "checkbox")
        colorization.colorize_item(self.ID.ID_ip, "node_sub")
        colorization.colorize_item(self.ID.ID_motor_speed, "node_sub")
        colorization.colorize_item(self.ID.ID_wallet, "node_sub")
    def init_values(self):
        add = element.object.misc.wallet.logic.get_add_from_ip(param_control.state_ground[self.ID.name]["info"]["ip"])
        param_control.state_ground[self.ID.name]["info"]["add"] = add
        dpg.set_value(self.ID.ID_wallet, add)

    # Command function
    def save_coord_to_file(self):
        pose = parser_json.get_pos_from_json()
        pose["ground"][self.ID.name] = dpg.get_item_pos(self.ID.ID_node)
        parser_json.upload_file(param_control.path_node_pose, pose)
    def command_new_add(self):
        add = dpg.get_value(self.ID.ID_wallet)
        ip = element.object.misc.wallet.logic.get_ip_from_add(add)
        if(ip != None):
            dpg.set_value(self.ID.ID_ip, ip)
            param_control.state_ground[self.ID.name]["info"]["ip"] = ip
            param_control.state_ground[self.ID.name]["info"]["add"] = add
            https_client_post.post_state_edge("ground", param_control.state_ground)
    def command_motor_start(self):
        https_client_post.post_command(self.ID.name, "start")
    def command_motor_stop(self):
        https_client_post.post_command(self.ID.name, "stop")
    def command_motor_speed(self):
        speed = dpg.get_value(self.ID.ID_motor_speed)
        param_control.state_ground[self.ID.name]["speed"] = speed
        https_client_post.post_state_edge("ground", param_control.state_ground)
        https_client_post.post_command("ground", "reset")
    def command_parameter(self):
        param_control.state_ground[self.ID.name]["info"]["device"] = dpg.get_value(self.ID.ID_device_list)
        param_control.state_ground[self.ID.name]["info"]["activated"] = dpg.get_value(self.ID.ID_activated)
        param_control.state_ground[self.ID.name]["info"]["ip"] = dpg.get_value(self.ID.ID_ip)
        https_client_post.post_state_edge("ground", param_control.state_ground)
        https_client_post.post_command("ground", "reset")

    # Update function
    def update(self):
        self.update_info()
        self.update_device_list()
        self.update_lidar_stats()
    def update_info(self):
        colorization.colorize_status(self.ID.ID_status, param_control.state_ground[self.ID.name]["info"]["status"])
        colorization.colorize_onoff(self.ID.ID_motor_on, self.ID.ID_motor_off, param_control.state_ground[self.ID.name]["motor"]["running"])
        dpg.configure_item(self.ID.ID_wallet, items=element.object.misc.wallet.logic.get_list_add())
        dpg.set_value(self.ID.ID_status, param_control.state_ground[self.ID.name]["info"]["status"])
        dpg.set_value(self.ID.ID_ip, param_control.state_ground[self.ID.name]["info"]["ip"])
    def update_device_list(self):
        devices = io.get_list_device_from_state()
        dpg.configure_item(self.ID.ID_device_list, default_value=param_control.state_ground[self.ID.name]["info"]["device"], items=devices, num_items=len(devices))
    def update_lidar_stats(self):
        dpg.set_value(self.ID.ID_stat_packet, param_control.state_ground[self.ID.name]["packet"]["value"])
        value = "%.2f"% param_control.state_ground[self.ID.name]["throughput"]["value"]
        min = param_control.state_ground[self.ID.name]["throughput"]["min"]
        mean = param_control.state_ground[self.ID.name]["throughput"]["mean"]
        max = param_control.state_ground[self.ID.name]["throughput"]["max"]
        range = "%.3f, %.3f, %.3f"% (min, mean, max)
        dpg.set_value(self.ID.ID_throughtput_value, value)
        dpg.set_value(self.ID.ID_throughtput_range, range)
