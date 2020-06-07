import constants
from entities.bacteriophages.bacteriophage import Bacteriophage


class B_Pult(Bacteriophage):
    def __init__(self):
        super().__init__(constants.GAME_WIDTH - 125, constants.CENTER_Y,
                         125, 125, 7, 100, 9, constants.B_PULT, 1, 2)
