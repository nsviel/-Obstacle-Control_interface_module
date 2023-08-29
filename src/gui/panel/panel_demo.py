#---------------------------------------------
import dearpygui.dearpygui as dpg
import dearpygui.demo as demo


class Demo:
    def __init__(self):
        self.is_init = False
        self.is_shown = False

    def demo(self):
        if(self.is_init == False):
            demo.show_demo()
            self.is_init = True
            self.is_shown = True
        elif(self.is_shown == True):
            dpg.hide_item("__demo_id")
            self.is_shown = False
        elif(self.is_shown == False):
            dpg.show_item("__demo_id")
            self.is_shown = True
