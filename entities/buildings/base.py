import constants
from entities.mortal import Mortal

Y_LOCATION = constants.GAME_HEIGHT // 4
WIDTH = 100
HEIGHT = constants.GAME_HEIGHT // 2

OFFSET = 550


class Base(Mortal):
    def __init__(self, allegiance, hp=100):
        x_location = constants.GAME_WIDTH // 2 - WIDTH // 2
        if allegiance == constants.MACROPHAGE_SIDE:
            x_location -= OFFSET
            name = "macrophage_base"
        elif allegiance == constants.BACTERIOPHAGE_SIDE:
            x_location += OFFSET
            name = "bacteriophage_base"
        else:
            raise ValueError("Wrong allegiance passed to Base.__init__().")
        super().__init__(x_location, Y_LOCATION, WIDTH, HEIGHT, hp, name, "static")
        self._allegiance = allegiance
