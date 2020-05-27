import constants
from entities.bacteriophages.bacteriophage import Bacteriophage


class B_Basic(Bacteriophage):
    def __init__(self):
        super().__init__(constants.GAME_WIDTH - 100, constants.GAME_HEIGHT / 2,
                         100, 125, 5, 1, 1, "buffteriophage", "walk", 5)
