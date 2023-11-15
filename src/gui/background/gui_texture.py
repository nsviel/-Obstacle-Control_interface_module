#---------------------------------------------
from src.param import param_control
from src.gui.background import gui_ID
from src.utils import function
import dearpygui.dearpygui as dpg


def get_path_from_icon_name(name):
    path_texture = "src/param/texture/"
    if(name == "wifi"):
        path = path_texture + "wifi.png"
    elif(name == "cloud"):
        path = path_texture + "cloud.png"
    elif(name == "lidar"):
        path = path_texture + "lidar.png"
    elif(name == "server"):
        path = path_texture + "server.png"
    elif(name == "train"):
        path = path_texture + "train.png"
    elif(name == "computer"):
        path = path_texture + "computer.png"
    elif(name == "compute"):
        path = path_texture + "compute.png"
    elif(name == "image_empty"):
        path = path_texture + "image_empty"
    elif(name == "software"):
        path = path_texture + "compute.png"
    elif(name == "ssd"):
        path = path_texture + "ssd.png"
    elif(name == "database"):
        path = path_texture + "database.png"
    elif(name == "hub"):
        path = path_texture + "hub.png"
    elif(name == "hdd"):
        path = path_texture + "hdd.png"
    elif(name == "gear"):
        path = path_texture + "gear.png"
    else:
        print("[error] texture name notrecognized: %s"% name)
    return path

def load_texture(name):
    try:
        path = get_path_from_icon_name(name)
        ID_tag = function.id_generator();
        w, h, c, i = dpg.load_image(path)
        with dpg.texture_registry():
            dpg.add_raw_texture(w, h, i, format=dpg.mvFormat_Float_rgba, tag=ID_tag)
    except:
        print("[error] texture path: %s"% path)
    return ID_tag
