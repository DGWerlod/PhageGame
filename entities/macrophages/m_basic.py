import constants
from entities.macrophages.macrophage import Macrophage


class M_Basic(Macrophage):
    def __init__(self):
        super().__init__(constants.GAME_WIDTH - 100, constants.GAME_HEIGHT / 2,
                         100, 125, 5, 1, 1, "macrophoot", "walk", 5)
