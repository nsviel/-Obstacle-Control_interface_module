#---------------------------------------------
from src.utils import function


class SSD:
    # Info
    ID_status = function.id_generator();
    ID_status_light = function.id_generator();
    ID_activated = function.id_generator();
    ID_parameter_visibility = function.id_generator();

    # Setting
    ID_memory_used = function.id_generator();
    ID_memory_total = function.id_generator();

    # Path
    ID_file_name = function.id_generator();
    ID_path = function.id_generator();
    ID_path_add = function.id_generator();

    ID_file_l1_size = function.id_generator();
    ID_path_l1 = function.id_generator();
    ID_path_l1_visibility = function.id_generator();

    ID_file_l2_size = function.id_generator();
    ID_path_l2 = function.id_generator();
    ID_path_l2_visibility = function.id_generator();
