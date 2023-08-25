#---------------------------------------------
from src.element.misc.wallet import wallet
from src.element.misc.block import block
from src.element.misc.link import link


class Misc:
    def __init__(self, ID):
        self.ID_misc = "misc_" + str(ID)
        self.wallet = wallet.Wallet()
        self.block = block.Block()
        self.link = link.Link()

    def build_windows(self):
        self.wallet.window.build()

    def build_nodes(self):
        pass

    def setup_handlers(self):
        pass
