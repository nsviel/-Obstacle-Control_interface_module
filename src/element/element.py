#---------------------------------------------
from src.param import param_control
from src.element.ground import ground
from src.element.edge import edge
from src.element.cloud import cloud
from src.element.misc import misc


class Element():
    def init_objects(self):
        self.ground = ground.Ground(1)
        self.edge_1 = edge.Edge(1)
        self.edge_2 = edge.Edge(2)
        self.cloud = cloud.Cloud(1)
        self.misc = misc.Misc(1)

    def build_windows(self):
        self.ground.build_windows()
        self.edge_1.build_windows()
        self.edge_2.build_windows()
        self.cloud.build_windows()
        self.misc.build_windows()

    def build_nodes(self):
        self.ground.build_nodes()
        self.edge_1.build_nodes()
        self.edge_2.build_nodes()
        self.cloud.build_nodes()
        self.misc.build_nodes()

    def setup_handlers(self):
        self.ground.setup_handlers()
        self.edge_1.setup_handlers()
        self.edge_2.setup_handlers()
        self.cloud.setup_handlers()
        self.misc.setup_handlers()

    def setup_links(self):
        self.ground.link.setup()
        self.edge_1.link.setup(self.ground, self.cloud)
        self.edge_2.link.setup(self.ground, self.cloud)
        self.cloud.link.setup(self.edge_1, self.edge_2)

        self.update_links()

    def update_links(self):
        self.ground.link.update()
        self.edge_1.link.update()
        self.edge_2.link.update()
        self.cloud.link.update()

object = Element()
