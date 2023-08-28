#---------------------------------------------
import dearpygui.dearpygui as dpg


def add_node_handler(ID, window):
    with dpg.item_handler_registry(tag=ID.ID_node_handler):
        dpg.add_item_clicked_handler(callback=window.set_visible)
        dpg.add_item_hover_handler(callback=window.update_info)
    dpg.bind_item_handler_registry(ID.ID_node, ID.ID_node_handler)
