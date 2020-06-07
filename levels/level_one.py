import constants
from entities.buildings.base import Base
from entities.buildings.wall import get_walls
from levels.level import Level


class Level_One(Level):
    def __init__(self):
        super().__init__(

            1,

            [
                constants.M_BASIC,
                constants.M_BEACH
            ],
            get_walls(constants.MACROPHAGE_SIDE),
            Base(constants.MACROPHAGE_SIDE),

            [
                constants.B_BASIC,
                constants.B_PULT,
                constants.B_TANK
            ],
            get_walls(constants.BACTERIOPHAGE_SIDE),
            Base(constants.BACTERIOPHAGE_SIDE)

        )
