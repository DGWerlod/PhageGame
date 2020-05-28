import constants
from entities.mortal import Mortal


class Wall(Mortal):
    def __init__(self, x, y, hp, allegiance, tier_number):
        if allegiance == constants.MACROPHAGE_SIDE:
            name = "macrophage_wall" + str(tier_number)
        elif allegiance == constants.BACTERIOPHAGE_SIDE:
            name = "bacteriophage_wall" + str(tier_number)
        else:
            raise ValueError("Wrong allegiance passed to Wall.__init__().")
        super().__init__(x, y, 50, 200, hp, name, "static")
        self._allegiance = allegiance
        self._tier_number = tier_number
