import constants
from controls import mouse
from entities.buttons.summoner import Summoner
from entities.microbes.microbe_builder import build_microbe
from logic import collisions, graphics

POSSIBLE_UPGRADES = set()


def _first_in_front_of_second(first, second, base_is_at_left):
    if second is None:
        return True
    first_x = first.get_rect().X
    second_x = second.get_rect().X
    output = False
    if base_is_at_left:
        first_w = first.get_rect().W
        second_w = second.get_rect().W
        output = first_x + first_w > second_x + second_w
    elif not base_is_at_left:
        output = first_x < second_x
    else:
        ValueError("Invalid input for parameter base_is_at_left.")
    return output


def _get_mortal_in_front(microbes, walls, base, base_is_at_left):
    in_front = None
    for w in walls:
        if _first_in_front_of_second(w, in_front, base_is_at_left):
            in_front = w
    for m in microbes:
        if _first_in_front_of_second(m, in_front, base_is_at_left):
            in_front = m
    if _first_in_front_of_second(base, in_front, base_is_at_left):
        in_front = base
    return in_front


def _microbe_actions(window, now, projectiles, enemies, enemy_walls, enemy_base, enemy_side):
    now_remaining = set()
    for n in now:
        in_front = _get_mortal_in_front(enemies, enemy_walls, enemy_base, enemy_side)
        n.set_in_front(in_front)
        n.go(window)
        if not enemy_side:  # now are macrophages
            on_screen = n.get_rect().X < constants.GAME_WIDTH
        elif enemy_side:  # now are bacteriophages
            n_rect = n.get_rect()
            on_screen = n_rect.X + n_rect.W > 0
        else:
            raise ValueError("Unrecognized enemy_side.")
        if n.is_alive() and on_screen:
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
                microbes.add(build_microbe(s.get_name()))
        s.go(window)


def _projectile_actions(window, projectiles,
                        macrophages, macrophage_walls, macrophage_base,
                        bacteriophages, bacteriophage_walls, bacteriophage_base):
    projectiles_remaining = set()
    for p in projectiles:
        allegiance = p.get_allegiance()
        if p.get_allegiance() == constants.MACROPHAGE_SIDE:
            in_front = _get_mortal_in_front(bacteriophages, bacteriophage_walls,
                                            bacteriophage_base, constants.BACTERIOPHAGE_SIDE)
        elif p.get_allegiance() == constants.BACTERIOPHAGE_SIDE:
            in_front = _get_mortal_in_front(macrophages, macrophage_walls,
                                            macrophage_base, constants.MACROPHAGE_SIDE)
        else:
            raise AssertionError("Wrong allegiance retrieved from Projectile.get_allegiance()")
        p.set_in_front(in_front)
        p.go(window)
        if allegiance:  # p is a macrophage projectile
            on_screen = p.get_rect().X < constants.GAME_WIDTH
        else:  # p is a bacteriophage projectile
            p_rect = p.get_rect()
            on_screen = p_rect.X + p_rect.W > 0
        if p.is_active() and on_screen:
            projectiles_remaining.add(p)
    return projectiles_remaining


class Level(object):
    def __init__(self, macrophages_available, macrophage_walls, macrophage_base,
                 bacteriophages_available, bacteriophage_walls, bacteriophage_base,
                 background=None, upgrades_enabled=None):

        self._macrophages = set()
        self._macrophages_available = macrophages_available
        self._macrophage_walls = macrophage_walls
        self._macrophage_base = macrophage_base
        self._macrophage_summoners = []

        self._bacteriophages = set()
        self._bacteriophages_available = bacteriophages_available
        self._bacteriophage_walls = bacteriophage_walls
        self._bacteriophage_base = bacteriophage_base
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
        if not self._bacteriophage_base.is_alive():
            return 1
        if not self._macrophage_base.is_alive():
            return -1
        return 0

    def go(self, window):
        if self._background:
            window.blit(self._background, (0, constants.HUD_HEIGHT))
        else:
            graphics.fill_game_rect(window, constants.BLUE)

        _summoner_actions(window, self._macrophage_summoners, self._macrophages)
        _summoner_actions(window, self._bacteriophage_summoners, self._bacteriophages)

        self._projectiles = _projectile_actions(window, self._projectiles, self._macrophages,
                                                self._macrophage_walls, self._macrophage_base,
                                                self._bacteriophages, self._bacteriophage_walls,
                                                self._bacteriophage_base)

        if self._macrophage_base.is_alive():
            self._macrophage_base.go(window)
        if self._bacteriophage_base.is_alive():
            self._bacteriophage_base.go(window)

        self._macrophage_walls = _wall_actions(window, self._macrophage_walls)
        self._bacteriophage_walls = _wall_actions(window, self._bacteriophage_walls)

        self._macrophages = _microbe_actions(window, self._macrophages, self._projectiles,
                                             self._bacteriophages, self._bacteriophage_walls,
                                             self._bacteriophage_base, constants.BACTERIOPHAGE_SIDE)
        self._bacteriophages = _microbe_actions(window, self._bacteriophages, self._projectiles,
                                                self._macrophages, self._macrophage_walls,
                                                self._macrophage_base, constants.MACROPHAGE_SIDE)
