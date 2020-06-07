import constants
from entities.mortal import Mortal

WIDTH = 90
HEIGHT = constants.GAME_HEIGHT // 8 * 3
Y_LOCATION = constants.HUD_HEIGHT + HEIGHT

HEALTH_BAR_OFFSET = 15

TIER_OFFSETS = [
    None,  # no such thing as tier zero!
    150,
    275,
    400
]


class Wall(Mortal):
    def __init__(self, allegiance, tier_number, hp=100):
        x_location = constants.GAME_WIDTH // 2 - WIDTH // 2
        if allegiance == constants.MACROPHAGE_SIDE:
            x_location -= TIER_OFFSETS[tier_number]
            name = "macrophage_wall"
        elif allegiance == constants.BACTERIOPHAGE_SIDE:
            x_location += TIER_OFFSETS[tier_number]
            name = "bacteriophage_wall"
        else:
            raise ValueError("Wrong allegiance passed to Wall.__init__().")
        super().__init__(x_location, Y_LOCATION, WIDTH, HEIGHT, hp, HEALTH_BAR_OFFSET, name, "static")
        self._allegiance = allegiance
        self._tier_number = tier_number

    def get_allegiance(self):
        return self._allegiance
