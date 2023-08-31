from src.base import daemon
from src.element import element


class Scheme_update(daemon.Daemon):
    def __init__(self):
        self.name = "Scheme update";
        self.run_sleep = 0.1;

    def thread_function(self):
        element.object.update_links()
        element.object.update_link_dependencies()
        element.object.update_nodes()
        element.object.update_windows()
