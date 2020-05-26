import constants
from entities.entity import Entity


class Wall(Entity):
    def __init__(self, x, y, hp, allegiance, tier_number):
        if allegiance == constants.MACROPHAGE_SIDE:
            name = "macrophage_wall" + tier_number
        elif allegiance == constants.BACTERIOPHAGE_SIDE:
            name = "bacteriophage_wall" + tier_number
        else:
            raise ValueError("Wrong allegiance passed to Wall.__init__().")
        super().__init__(x, y, 50, 200, name)
        self._hp = hp
        self._allegiance = allegiance
        self._tier_number = tier_number
