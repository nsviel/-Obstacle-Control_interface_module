#---------------------------------------------
from src.element.misc.wallet import wallet
from src.element.misc.block import block


class Misc:
    def __init__(self, ID):
        self.ID_misc = "misc_" + str(ID)
        self.wallet = wallet.Wallet()
        self.block = block.Block()

    def build_windows(self):
        self.wallet.window.build()

    def build_nodes(self):
        self.block.design_blocks()

    def setup_handlers(self):
        pass

    def set_invisible_all(self):
        self.wallet.window.set_invisible()
