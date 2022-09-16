#---------------------------------------------
from param import param_co
import dearpygui.dearpygui as dpg


def init_image():
    try:
        width, height, channels, data = dpg.load_image(param_co.path_image)

        with dpg.texture_registry():
            dpg.add_dynamic_texture(width, height, data, tag="image_in")
    except:
        print("[\033[1;31merror\033[0m] No image at \033[1;36m%s\033[0m" % param_co.path_image)
        exit()
