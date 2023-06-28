#---------------------------------------------
from src.scheme.node.interface import node_module_interface
from src.scheme.node.train import node_module_capture
from src.scheme.node.train import node_train
from src.scheme.node.edge import node_edge
from src.scheme.node.edge import node_edge_1
from src.scheme.node.edge import node_edge_2
from src.scheme.node.edge import node_data_processing
from src.scheme.node.interface import node_network
from src.scheme.node.edge import node_ai
from src.scheme.node.cloud import node_operator
from src.scheme.node.cloud import node_cloud
from src.scheme.node.interface import node_ssd
from src.scheme.node.data import node_data


def create_node():
    node_train.design_block()
    node_edge.design_block()
    node_cloud.design_block()

    node_module_interface.design_node()
    node_module_capture.design_node()
    node_edge_1.design_node()
    node_edge_2.design_node()
    node_train.design_node()
    node_data_processing.design_node()
    node_ai.design_node()
    node_operator.design_node()
    node_cloud.design_node()
    node_ssd.design_node()
    node_data.design_node()
    node_network.design_node()
