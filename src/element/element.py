#---------------------------------------------
from src.param import param_control
from src.element.ground import ground
from src.element.edge import edge
from src.element.cloud import cloud
from src.element.misc import misc


class Element():
    def init_objects(self):
        self.misc = misc.Misc(1)
        self.ground = ground.Ground(1)
        self.edge = edge.Edge(1)
        self.cloud = cloud.Cloud(1)

    # Window
    def build_windows(self):
        self.ground.build_windows()
        self.edge.build_windows()
        self.cloud.build_windows()
        self.misc.build_windows()
    def update_windows(self):
        self.ground.update_windows()
        self.edge.update_windows()
        self.cloud.update_windows()
        self.misc.update_windows()

    # Node
    def build_nodes(self):
        self.ground.build_nodes()
        self.edge.build_nodes()
        self.cloud.build_nodes()
        self.misc.build_nodes()
    def update_nodes(self):
        self.ground.update_nodes()
        self.edge.update_nodes()
        self.cloud.update_nodes()
    def position_nodes(self):
        self.ground.position_nodes()
        self.edge.position_nodes()
        self.cloud.position_nodes()

    # Event
    def setup_handlers(self):
        self.ground.setup_handlers()
        self.edge.setup_handlers()
        self.cloud.setup_handlers()
        self.misc.setup_handlers()
    def set_invisible_all(self):
        self.ground.set_invisible_all()
        self.edge.set_invisible_all()
        self.cloud.set_invisible_all()
        self.misc.set_invisible_all()

    # Link
    def setup_links(self):
        self.ground.link.setup()
        self.edge.link.setup(self.ground, self.cloud)
        self.cloud.link.setup(self.edge)
    def update_links(self):
        self.ground.link.update()
        self.edge.link.update()
        self.cloud.link.update()

    # Update
    def update_scheme(self):
        self.update_links()
        self.update_nodes()
        self.update_windows()





object = Element()
