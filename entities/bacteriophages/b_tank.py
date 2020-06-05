import constants
from entities.bacteriophages.bacteriophage import Bacteriophage


class B_Tank(Bacteriophage):
    def __init__(self):
        super().__init__(constants.GAME_WIDTH - 125, constants.CENTER_Y,
                         125, 125, 5, 200, 10, constants.B_TANK, 2, 2)

    def pos(self):
        if self._animation_cycle == 3:
            self._x -= self._spd * 3
        if self._animation_cycle == 4:
            self._x -= self._spd * 2
        
