import constants
from entities.microbes.macrophages.macrophage import Macrophage


class M_Beach(Macrophage):
    def __init__(self):
        super().__init__(0, constants.CENTER_Y, 125, 125, constants.M_BEACH, 1, 2)
