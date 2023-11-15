#---------------------------------------------
from src.param import param_control
from src.connection.HTTPS.client import https_client_get
from src.base import daemon
from src.element import element
import dearpygui.dearpygui as dpg


class Data_image(daemon.Daemon):
    def __init__(self):
        self.name = "Data image";

    def thread_function(self):
        # Load current image
        image_acquired = https_client_get.get_image("edge")

        # Update image
        if(image_acquired):
            element.object.edge.data.node.update_image()
