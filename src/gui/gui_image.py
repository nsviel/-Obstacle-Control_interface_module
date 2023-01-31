#---------------------------------------------
from src.param import param_co
import dearpygui.dearpygui as dpg


def init_image():
    try:
        data_w, data_h, data_c, data_i = dpg.load_image(param_co.path_image_empty)

        computer_w, computer_h, computer_c, computer_i = dpg.load_image(param_co.path_icon_computer)
        wifi_w, wifi_h, wifi_c, wifi_i = dpg.load_image(param_co.path_icon_wifi)
        lidar_w, lidar_h, lidar_c, lidar_i = dpg.load_image(param_co.path_icon_lidar)
        server_w, server_h, server_c, server_i = dpg.load_image(param_co.path_icon_server)
        train_w, train_h, train_c, train_i = dpg.load_image(param_co.path_icon_train)
        cloud_w, cloud_h, cloud_c, cloud_i = dpg.load_image(param_co.path_icon_cloud)
        soft_w, soft_h, soft_c, soft_i = dpg.load_image(param_co.path_icon_soft)
        ssd_w, ssd_h, ssd_c, ssd_i = dpg.load_image(param_co.path_icon_ssd)

        param_co.image_w = data_w
        param_co.image_h = data_h

        with dpg.texture_registry():
            dpg.add_raw_texture(data_w, data_h, data_i, format=dpg.mvFormat_Float_rgba, tag="image_in")
            dpg.add_raw_texture(computer_w, computer_h, computer_i, format=dpg.mvFormat_Float_rgba, tag="icon_computer")
            dpg.add_raw_texture(wifi_w, wifi_h, wifi_i, format=dpg.mvFormat_Float_rgba, tag="icon_wifi")
            dpg.add_raw_texture(lidar_w, lidar_h, lidar_i, format=dpg.mvFormat_Float_rgba, tag="icon_lidar")
            dpg.add_raw_texture(server_w, server_h, server_i, format=dpg.mvFormat_Float_rgba, tag="icon_server")
            dpg.add_raw_texture(train_w, train_h, train_i, format=dpg.mvFormat_Float_rgba, tag="icon_train")
            dpg.add_raw_texture(cloud_w, cloud_h, cloud_i, format=dpg.mvFormat_Float_rgba, tag="icon_cloud")
            dpg.add_raw_texture(soft_w, soft_h, soft_i, format=dpg.mvFormat_Float_rgba, tag="icon_soft")
            dpg.add_raw_texture(ssd_w, ssd_h, ssd_i, format=dpg.mvFormat_Float_rgba, tag="icon_ssd")
    except:
        print("[\033[1;31merror\033[0m] Image & icon loading")
        exit()
