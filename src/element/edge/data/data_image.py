#---------------------------------------------
from src.param import param_control
from src.connection.HTTPS.client import https_client_get
from src.base import daemon
import dearpygui.dearpygui as dpg


class Data_image(daemon.Daemon):
    def thread_function(self):
        pass
        # Load current image
        #image_acquired = https_client_get.get_image("edge")

        # Update image
        #if(image_acquired):
        #    self.update_image()

    def update_image(self):
        # Update image but if format problem close the program
        width, height, channels, data = dpg.load_image(param_control.path_state_current + "image")
        try:
            dpg.set_value("image_in", data)
        except:
            print("[\033[1;31merror\033[0m] Image dimension error")
            param_control.run_loop = False
