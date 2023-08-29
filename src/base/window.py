#---------------------------------------------
from src.param import param_control
from src.element import element
from src.gui.background import gui_ID
from src.gui.style import gui_color
from src.utils import parser_json
import dearpygui.dearpygui as dpg


class Window:
    def __init__(self, ID):
        self.ID = ID

    # Build function
    def build(self):
        with dpg.child_window(tag=self.ID.ID_window_info, parent=gui_ID.ID_panel_setting, border=False, autosize_x=True, height=75):
            self.build_info()
        with dpg.child_window(tag=self.ID.ID_window_parameter, parent=gui_ID.ID_panel_setting, border=False, autosize_x=True):
            self.build_parameter()
        self.set_initial_state()

    def set_initial_state(self):
        self.set_invisible()
        theme = gui_color.color_window_info()
        dpg.bind_item_theme(self.ID.ID_window_info, theme)

    def build_info(self):
        with dpg.table(tag=self.ID.ID_window_table_info, header_row=False, borders_innerH=True, policy=dpg.mvTable_SizingFixedFit):
            dpg.add_table_column(width_fixed=True, init_width_or_weight=50)
            dpg.add_table_column(width_fixed=True, init_width_or_weight=160)
            dpg.add_table_column(width_fixed=True, init_width_or_weight=20)
            with dpg.table_row():
                dpg.add_text("Node")
                dpg.add_text(self.ID.name, color=(0, 200, 50))
                dpg.add_button(label="X", callback=self.set_invisible)
            with dpg.table_row():
                dpg.add_text("Status");
                dpg.add_text("-", tag=self.ID.ID_status);
            with dpg.table_row():
                dpg.add_text("Pose")
                dpg.add_text(tag=self.ID.ID_node_coord)
                dpg.add_button(label="s", callback=self.save_coord_to_file)
        dpg.add_separator()
    def build_parameter(self):
        pass

    # Update function
    def update(self):
        self.update_pose()
        self.update_parameter()
    def update_pose(self):
        coord = dpg.get_item_pos(self.ID.ID_node)
        dpg.set_value(self.ID.ID_node_coord, coord)
    def update_parameter(self):
        pass

    # Subfunction
    def set_visible(self):
        element.object.set_invisible_all()
        dpg.show_item(self.ID.ID_window_info)
        dpg.show_item(self.ID.ID_window_parameter)
    def set_invisible(self):
        dpg.hide_item(self.ID.ID_window_info)
        dpg.hide_item(self.ID.ID_window_parameter)
    def save_coord_to_file(self):
        pass
