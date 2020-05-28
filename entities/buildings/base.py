import constants
from entities.mortal import Mortal


class Base(Mortal):
    def __init__(self, x, y, hp, allegiance):
        if allegiance == constants.MACROPHAGE_SIDE:
            name = "macrophage_base"
        elif allegiance == constants.BACTERIOPHAGE_SIDE:
            name = "bacteriophage_base"
        else:
            raise ValueError("Wrong allegiance passed to Base.__init__().")
        super().__init__(x, y, 100, 200, hp, name, "static")
        self._allegiance = allegiance
