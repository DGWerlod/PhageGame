import constants
from entities.bacteriophages.bacteriophage import Bacteriophage


class B_Tank(Bacteriophage):
    def __init__(self):
        super().__init__(constants.GAME_WIDTH - 125, constants.CENTER_Y,
                         125, 125, 5, 200, 10, constants.B_TANK, 2, 2)

    def pos(self):
        # current frame to be displayed is the floor of this value divided by _animation_spd
        cur_frame = (self._animation_cycle + 1) // self._animation_spd
        if cur_frame == 2:
            self._x -= self._spd * 3
        if cur_frame == 3:
            self._x -= self._spd * 2
        
