import constants
from entities.buildings.base import Base
from entities.buildings.wall import Wall
from levels.level import Level
from img.images import IMAGES


class Level_One(Level):
    def __init__(self):

        super().__init__({constants.M_BASIC},
                         [
                             Wall(constants.MACROPHAGE_SIDE, 3),
                             Wall(constants.MACROPHAGE_SIDE, 2),
                             Wall(constants.MACROPHAGE_SIDE, 1)
                         ],
                         Base(constants.MACROPHAGE_SIDE),

                         {constants.B_BASIC},
                         [
                             Wall(constants.BACTERIOPHAGE_SIDE, 3),
                             Wall(constants.BACTERIOPHAGE_SIDE, 2),
                             Wall(constants.BACTERIOPHAGE_SIDE, 1)
                         ],
                         Base(constants.BACTERIOPHAGE_SIDE),

                         None,
                         
                         IMAGES["level"]["background"][0])
