import constants
from entities.macrophages.macrophage import Macrophage


class M_Basic(Macrophage):
    def __init__(self):
        super().__init__(0, constants.GAME_HEIGHT / 2, 100, 125, 5, 100, 13, "macrophoot", 5, 2)
