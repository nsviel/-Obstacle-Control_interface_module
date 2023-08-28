#---------------------------------------------
from src.param import param_control
from src.gui.background import gui_ID
from src.gui.style import gui_color
from src.utils import parser_json
import dearpygui.dearpygui as dpg


class Window:
    def __init__(self, ID):
        self.ID = ID
        self.is_visible = False

    # Build function
    def build(self):
        with dpg.child_window(tag=self.ID.ID_window, parent=gui_ID.ID_panel_setting, border=True, height=250, autosize_x=True):
            self.build_info()
            self.build_parameter()
        
        dpg.hide_item(self.ID.ID_window)
    def build_info(self):
        dpg.add_separator()
        with dpg.table(header_row=False, borders_innerH=True, policy=dpg.mvTable_SizingFixedFit):
            dpg.add_table_column(label="What", width_fixed=True, init_width_or_weight=50)
            dpg.add_table_column(label="Value", width_fixed=True, init_width_or_weight=100)
            dpg.add_table_column(label="Button", width_fixed=True, init_width_or_weight=20)
            with dpg.table_row():
                dpg.add_text("Node")
                dpg.add_text(self.ID.name, color=gui_color.color_title)
                dpg.add_button(label="X", callback=self.switch_visibility)
            with dpg.table_row():
                dpg.add_text("Status");
                dpg.add_text("-", tag=self.ID.ID_status, color=gui_color.color_info);
            with dpg.table_row():
                dpg.add_text("Pose")
                dpg.add_text(tag=self.ID.ID_node_coord)
                dpg.add_button(label="s", callback=self.save_coord_to_file)
        dpg.add_separator()
        dpg.add_separator()
    def build_parameter(self):
        pass

    # Update function
    def update(self):
        self.update_info()
        self.update_parameter()
    def update_info(self):
        coord = dpg.get_item_pos(self.ID.ID_node)
        dpg.set_value(self.ID.ID_node_coord, coord)
    def update_parameter(self):
        pass

    # Subfunction
    def switch_visibility(self):
        if(self.is_visible):
            dpg.hide_item(self.ID.ID_window)
            self.is_visible = False
        else:
            dpg.show_item(self.ID.ID_window)
            self.is_visible = True
    def save_coord_to_file(self):
        pass
