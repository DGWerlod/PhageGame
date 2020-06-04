import constants
from entities.bacteriophages.bacteriophage import Bacteriophage


class B_Basic(Bacteriophage):
    def __init__(self):
        super().__init__(constants.GAME_WIDTH - 125, constants.CENTER_Y,
                         125, 125, 5, 100, 9, constants.B_BASIC, 5, 2)
