#---------------------------------------------
from src.param import param_control
from src.base import window
from src.gui.background import gui_ID
from src.gui.style import gui_color
from src.utils import parser_json
import dearpygui.dearpygui as dpg


class Ssd_window(window.Window):
    # Build function
    def build_parameter(self):
        with dpg.table(header_row=False, borders_innerH=True):
            dpg.add_table_column()
            dpg.add_table_column()
            with dpg.table_row():
                dpg.add_text("SSD saving");
                dpg.add_checkbox(tag=self.ID.ID_activated, label="", default_value=False, callback=self.command_ssd)
            with dpg.table_row():
                dpg.add_text("Path")
                dpg.add_input_text(tag=self.ID.ID_path, label="", default_value="", width=200, on_enter=True, callback=self.command_ssd_editing)
            with dpg.table_row():
                dpg.add_text("Memory");
                with dpg.group(horizontal=True):
                    dpg.add_text(0, tag=self.ID.ID_memory_used, color=gui_color.color_info);
                    dpg.add_text("/");
                    dpg.add_text(0, tag=self.ID.ID_memory_total, color=gui_color.color_info);
                    dpg.add_text("Gb");
        dpg.add_separator()
        with dpg.table(header_row=False, borders_innerH=True):
            dpg.add_table_column()
            dpg.add_table_column()
            with dpg.table_row():
                dpg.add_text("File", color=gui_color.color_title)
                dpg.add_button(label="New save", width=100, callback=self.command_new_save)
            with dpg.table_row():
                dpg.add_text("Name");
                dpg.add_input_text(tag=self.ID.ID_path_add, label="", default_value="", width=200, on_enter=True, callback=self.command_ssd_editing)
            with dpg.table_row():
                dpg.add_text("Fullname")
                dpg.add_text("-", tag=self.ID.ID_file_name, color=gui_color.color_info)
        dpg.add_separator()

        # LiDAR 1
        dpg.add_text("Lidar 1", color=gui_color.color_title)
        with dpg.table(header_row=False, borders_innerH=True):
            dpg.add_table_column()
            dpg.add_table_column()
            with dpg.table_row():
                dpg.add_text("-", tag=self.ID.ID_path_l1, color=gui_color.color_info)
            with dpg.table_row():
                dpg.add_text("Size")
                with dpg.group(horizontal=True):
                    dpg.add_text(0, tag=self.ID.ID_file_l1_size, color=gui_color.color_info)
                    dpg.add_text("Gb");

        # LiDAR 2
        dpg.add_separator()
        dpg.add_text("Lidar 2", color=gui_color.color_title)
        with dpg.table(header_row=False, borders_innerH=True):
            dpg.add_table_column()
            dpg.add_table_column()
            with dpg.table_row():
                dpg.add_text("-", tag=self.ID.ID_path_l2, color=gui_color.color_info)
            with dpg.table_row():
                dpg.add_text("Size")
                with dpg.group(horizontal=True):
                    dpg.add_text(0, tag=self.ID.ID_file_l2_size, color=gui_color.color_info)
                    dpg.add_text("Gb");
        dpg.add_separator()
    def colorize_window(self):
        colorization.colorize_item(self.ID.ID_activated, "checkbox")
        colorization.colorize_item(self.ID.ID_path_add, "input_text")
        colorization.colorize_item(self.ID.ID_path, "input_text")

    # Command function
    def command_new_save(self):
        saving.determine_path()
    def command_ssd_editing(self):
        param_control.state_control["ssd"]["path"]["file_name_add"] = dpg.get_value(self.ID.ID_path_add)
        param_control.path_ssd = dpg.get_value(self.ID.ID_path)
        saving.determine_path()
    def command_ssd(self):
        param_control.path_ssd = dpg.get_value(self.ID.ID_path)
        param_control.state_control["ssd"]["activated"] = dpg.get_value(self.ID.ID_activated)
    def save_coord_to_file(self):
        pose = parser_json.get_pos_from_json()
        pose["cloud"]["ssd"] = dpg.get_item_pos(self.ID.ID_node)
        parser_json.upload_file(param_control.path_node_pose, pose)

    # Update function
    def update(self):
        pass
