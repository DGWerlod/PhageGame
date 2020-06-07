import constants
from entities.microbes.bacteriophages.bacteriophage import Bacteriophage
from entities.projectile import Projectile

class B_Pult(Bacteriophage):
    def __init__(self):
        super().__init__(constants.GAME_WIDTH - 125, constants.CENTER_Y,
                         125, 125, 7, 100, 0, constants.B_PULT, 1, 2)

    def make_projectile(self):
        return Projectile(self._x, self._y, 50, 50, 1, 10, self)