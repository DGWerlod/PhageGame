import constants
from entities.entity import Entity


class Base(Entity):
    def __init__(self, x, y, hp, allegiance):
        if allegiance == constants.MACROPHAGE_SIDE:
            name = "macrophage_base"
        elif allegiance == constants.BACTERIOPHAGE_SIDE:
            name = "bacteriophage_base"
        else:
            raise ValueError("Wrong allegiance passed to Base.__init__().")
        super().__init__(x, y, 100, 200, name)
        self._hp = hp
        self._allegiance = allegiance
