import constants
import properties
from entities.mortal import Mortal

Y_LOCATION = constants.HUD_HEIGHT + constants.GAME_HEIGHT // 4
WIDTH = 100
HEIGHT = constants.GAME_HEIGHT // 2

OFFSET = 550

HEALTH_BAR_OFFSET = 15


class Base(Mortal):
    def __init__(self, allegiance):
        x_location = constants.GAME_WIDTH // 2 - WIDTH // 2
        if allegiance == constants.MACROPHAGE_SIDE:
            x_location -= OFFSET
            name = "macrophage_base"
        elif allegiance == constants.BACTERIOPHAGE_SIDE:
            x_location += OFFSET
            name = "bacteriophage_base"
        else:
            raise ValueError("Wrong allegiance passed to Base.__init__().")
        hp = properties.base_hit_points[allegiance]
        super().__init__(x_location, Y_LOCATION, WIDTH, HEIGHT, hp, HEALTH_BAR_OFFSET, name, "static")
        self._allegiance = allegiance

    def get_allegiance(self):
        return self._allegiance
