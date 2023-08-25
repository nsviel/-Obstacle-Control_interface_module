#---------------------------------------------
from src.param import param_control
from src.connection.HTTPS import https_client_post
from src.element import element
import dearpygui.dearpygui as dpg
import dearpygui.demo as demo


def callback_demo():
    demo.show_demo()

def callback_close():
    param_control.run_loop = False

def callback_wallet():
    element.object.wallet.window.switch_visibility()
