#---------------------------------------------
from src.utils import function
from src.param import param_control
import dearpygui.dearpygui as dpg
import random


class Data_plot:
    def __init__(self, ID):
        self.ID = ID
        self.nb_tic = 1000
        self.vec_x = []
        self.vec_y_l1 = []
        self.vec_y_l2 = []
        self.init_plot()

    # Plot function
    def init_plot(self):
        for i in range(0, self.nb_tic):
            self.vec_x.append(i)
            self.vec_y_l1.append(0)
            self.vec_y_l2.append(0)
    def update_plot_l1(self, data_len):
        self.vec_y_l1.pop(0)
        self.vec_y_l1.append(data_len)
        dpg.set_value(self.ID.ID_plot_l1, [self.vec_x, self.vec_y_l1])
    def update_plot_l2(self, data_len):
        self.vec_y_l2.pop(0)
        self.vec_y_l2.append(data_len)
        dpg.set_value(self.ID.ID_plot_l2, [self.vec_x, self.vec_y_l2])
    def update_plot_random(self):
        self.vec_y_l1.pop(0)
        self.vec_y_l2.pop(0)

        self.vec_y_l1.append(random.randint(0, 1248))
        self.vec_y_l2.append(random.randint(0, 1248))

        dpg.set_value('l1_plot', [self.vec_x, self.vec_y_l1])
        dpg.set_value('l2_plot', [self.vec_x, self.vec_y_l2])

    # Packet processing
    def process_l1_data(self, packet):
        path = param_control.state_control["ssd"]["path"]["path_l1_file"]
        self.update_plot_l1(len(packet))
    def process_l2_data(self, packet):
        path = param_control.state_control["ssd"]["path"]["path_l2_file"]
        self.update_plot_l2(len(packet))
