import constants
from entities.bacteriophages.bacteriophage import Bacteriophage


class B_Basic(Bacteriophage):
    def __init__(self):
        super().__init__(constants.GAME_WIDTH - 125, constants.GAME_HEIGHT / 2,
                         125, 125, 5, 100, 9, "buffteriophage", 5, 2)
