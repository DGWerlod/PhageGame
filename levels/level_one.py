import constants

from entities.buildings.base import Base
from entities.buildings.wall import get_walls
from entities.microbes.microbe_builder import build_microbe

from levels import level
from levels.level import Level
from logic.dice import Die

MACROPHAGES_ALLOWED = [
    constants.M_BASIC,
    constants.M_BEACH
]
BACTERIOPHAGES_ALLOWED = [
    constants.B_BASIC,
    constants.B_PULT,
    constants.B_TANK
]
FRAMES_BETWEEN_SPAWNS = 60


class Level_One(Level):
    def __init__(self, use_ai):
        super().__init__(

            1, use_ai,
            MACROPHAGES_ALLOWED,
            get_walls(constants.MACROPHAGE_SIDE),
            Base(constants.MACROPHAGE_SIDE),
            BACTERIOPHAGES_ALLOWED,
            get_walls(constants.BACTERIOPHAGE_SIDE),
            Base(constants.BACTERIOPHAGE_SIDE)

        )
        self._bacteriophage_die = Die(len(BACTERIOPHAGES_ALLOWED))
        self._until_next_spawn = FRAMES_BETWEEN_SPAWNS

    def ai(self):
        if self._until_next_spawn <= 0:
            unit_id = BACTERIOPHAGES_ALLOWED[self._bacteriophage_die.roll() - 1]
            if constants.SHOW_DEBUG:
                print("Level_One AI rolled a " + unit_id)
            self._bacteriophage_mortals[level.MICROBES].add(build_microbe(unit_id))
            self._until_next_spawn = FRAMES_BETWEEN_SPAWNS
        self._until_next_spawn -= 1
