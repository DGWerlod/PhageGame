import constants
from entities.macrophages.macrophage import Macrophage


class M_Basic(Macrophage):
    def __init__(self):
        super().__init__(0, constants.CENTER_Y, 125, 125, 6, 100, 13, constants.M_BASIC, 2, 2)
