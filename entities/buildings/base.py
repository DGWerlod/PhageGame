import constants
from entities.mortal import Mortal


class Base(Mortal):
    def __init__(self, x, hp, allegiance):
        if allegiance == constants.MACROPHAGE_SIDE:
            name = "macrophage_base"
        elif allegiance == constants.BACTERIOPHAGE_SIDE:
            name = "bacteriophage_base"
        else:
            raise ValueError("Wrong allegiance passed to Base.__init__().")
        super().__init__(x, constants.GAME_HEIGHT // 4, 100, constants.GAME_HEIGHT // 2, hp, name, "static")
        self._allegiance = allegiance
