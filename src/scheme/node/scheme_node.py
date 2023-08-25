#---------------------------------------------
from src.scheme.node.control import node_control
from src.scheme.node.train import node_capture
from src.scheme.node.train import node_train
from src.scheme.node.edge import block_edge
from src.scheme.node.edge import node_edge
from src.scheme.node.edge import node_edge_1
from src.scheme.node.edge import node_edge_2
from src.scheme.node.edge.component import node_slam
from src.scheme.node.control import node_network
from src.scheme.node.edge.component import node_ai
from src.scheme.node.cloud import node_operator
from src.scheme.node.cloud import node_cloud
from src.scheme.node.control import node_ssd
from src.scheme.node.edge.data import node_data
from src.scheme.object import object


def create_node():
    node_train.design_block()
    block_edge.design_block()
    node_cloud.design_block()

    node_control.design_node()
    node_capture.design_node()
    node_train.design_node()
    node_operator.design_node()
    node_cloud.design_node()
    node_ssd.design_node()
    node_network.design_node()

    node_edge.design_node(object.object.edge_1)
    node_edge.design_node(object.object.edge_2)
    node_data.design_node()
    node_slam.design_node()
    node_ai.design_node()
