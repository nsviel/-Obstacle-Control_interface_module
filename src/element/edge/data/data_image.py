#---------------------------------------------
from src.param import param_control
from src.connection.HTTPS import https_client_get
from src.utils import terminal
from src.utils import daemon


class Data_image(daemon.Daemon):
    def thread_function(self):
        # Load current image
        image_acquired = https_client_get.get_image("edge")

        # Update image
        if(image_acquired):
            update_image()

    name = "Image loader";
    run_sleep = 0.1;

    def update_image():
        # Update image but if format problem close the program
        width, height, channels, data = dpg.load_image(param_control.path_image)
        if(width == param_control.image_w and height == param_control.image_h):
            dpg.set_value("image_in", data)
        else:
            print("[\033[1;31merror\033[0m] Image dimension error [%d/%d] [%d/%d]"% (width, param_control.image_w, height, param_control.image_h))
            param_control.run_loop = False
