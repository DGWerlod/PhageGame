import constants
from entities.microbes.bacteriophages.bacteriophage import Bacteriophage
from entities.projectile import Projectile
from logic.dice import D20


class B_Pult(Bacteriophage):

    DIE = D20()

    def __init__(self):
        super().__init__(constants.GAME_WIDTH - 125, constants.CENTER_Y, 125, 125, constants.B_PULT, 1, 2)

    def make_projectile(self):
        return Projectile(self._x, self._y, 50, 50, 40, B_Pult.DIE.roll(), self)
