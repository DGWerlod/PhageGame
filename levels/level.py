import constants
from controls import mouse
from entities.buttons.summoner import Summoner
from entities.microbes.microbe_builder import build_microbe
from logic import collisions, graphics, positions

MICROBES = 0
WALLS = 1
BASE = 2
POSSIBLE_UPGRADES = set()


def _microbe_actions(window, now, projectiles, enemy_mortals):
    now_remaining = set()
    for n in now:
        in_front = positions.get_mortal_in_front(enemy_mortals, MICROBES, WALLS, BASE)
        n.set_in_front(in_front)
        n.go(window)
        if n.is_alive() and positions.is_on_screen(n):
            now_remaining.add(n)
        projectile = n.check_projectile()
        if projectile is not None:
            projectiles.add(projectile)
    return now_remaining


def _wall_actions(window, walls):
    walls_remaining = []
    for w in walls:
        if w.is_alive():
            walls_remaining.append(w)
            w.go(window)
    return walls_remaining


def _summoner_actions(window, summoners, microbes):
    for s in summoners:
        if mouse.controls['click'] and s.can_summon():
            if collisions.rect_point(s.get_rect(), mouse.controls['pos']):
                s.do_summon()
                microbes.add(build_microbe(s.get_unit_name()))
        s.go(window)


def _projectile_actions(window, projectiles, macrophage_mortals, bacteriophage_mortals):
    projectiles_remaining = set()
    for p in projectiles:
        allegiance = p.get_allegiance()
        if allegiance == constants.MACROPHAGE_SIDE:
            in_front = positions.get_mortal_in_front(bacteriophage_mortals, MICROBES, WALLS, BASE)
        elif allegiance == constants.BACTERIOPHAGE_SIDE:
            in_front = positions.get_mortal_in_front(macrophage_mortals, MICROBES, WALLS, BASE)
        else:
            raise AssertionError("Wrong allegiance retrieved from Projectile.get_allegiance()")
        p.set_in_front(in_front)
        p.go(window)
        if p.is_active() and positions.is_on_screen(p):
            projectiles_remaining.add(p)
    return projectiles_remaining


class Level(object):
    def __init__(self, macrophages_available, macrophage_walls, macrophage_base,
                 bacteriophages_available, bacteriophage_walls, bacteriophage_base,
                 background=None, upgrades_enabled=None):

        self._macrophage_mortals = [
            set(),  # microbes
            macrophage_walls,
            macrophage_base
        ]
        self._macrophage_summoners = []

        self._bacteriophage_mortals = [
            set(),  # microbes
            bacteriophage_walls,
            bacteriophage_base
        ]
        self._bacteriophage_summoners = []

        self._projectiles = set()

        self._background = background

        self._upgrades_enabled = upgrades_enabled

        x_loc = 0
        for m in macrophages_available:
            self._macrophage_summoners.append(Summoner(x_loc, constants.BOTTOM_HUD, 125, 125, m))
            x_loc += 125
        x_loc = constants.GAME_WIDTH - 125
        for b in bacteriophages_available:
            self._bacteriophage_summoners.append(Summoner(x_loc, constants.BOTTOM_HUD, 125, 125, b))
            x_loc -= 125

    # 1 is a victory, -1 is defeat, 0 is neither
    def check_winner(self):
        if not self._bacteriophage_mortals[BASE].is_alive():
            return 1
        if not self._macrophage_mortals[BASE].is_alive():
            return -1
        return 0

    def go(self, window):
        if self._background:
            window.blit(self._background, (0, constants.HUD_HEIGHT))
        else:
            graphics.fill_game_rect(window, constants.BLUE)

        _summoner_actions(window, self._macrophage_summoners, self._macrophage_mortals[MICROBES])
        _summoner_actions(window, self._bacteriophage_summoners, self._bacteriophage_mortals[MICROBES])

        if self._macrophage_mortals[BASE].is_alive():
            self._macrophage_mortals[BASE].go(window)
        if self._bacteriophage_mortals[BASE].is_alive():
            self._bacteriophage_mortals[BASE].go(window)

        self._macrophage_mortals[WALLS] = _wall_actions(window, self._macrophage_mortals[WALLS])
        self._bacteriophage_mortals[WALLS] = _wall_actions(window, self._bacteriophage_mortals[WALLS])

        self._macrophage_mortals[MICROBES] = _microbe_actions(window, self._macrophage_mortals[MICROBES],
                                                              self._projectiles, self._bacteriophage_mortals)
        self._bacteriophage_mortals[MICROBES] = _microbe_actions(window, self._bacteriophage_mortals[MICROBES],
                                                                 self._projectiles, self._macrophage_mortals)

        self._projectiles = _projectile_actions(window, self._projectiles, self._macrophage_mortals,
                                                self._bacteriophage_mortals)
