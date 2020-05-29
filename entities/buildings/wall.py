import constants
from entities.mortal import Mortal


class Wall(Mortal):
    def __init__(self, x, hp, allegiance, tier_number):
        if allegiance == constants.MACROPHAGE_SIDE:
            name = "macrophage_wall"
        elif allegiance == constants.BACTERIOPHAGE_SIDE:
            name = "bacteriophage_wall"
        else:
            raise ValueError("Wrong allegiance passed to Wall.__init__().")
        super().__init__(x, constants.GAME_HEIGHT // 8 * 3, 30, constants.GAME_HEIGHT // 8 * 3, hp, name, "static")
        self._allegiance = allegiance
        self._tier_number = tier_number
