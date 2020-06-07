import constants
from entities.entity import Entity
from entities.health_bar import Health_Bar


HEALTH_BAR_WIDTH = 75
HEALTH_BAR_HEIGHT = 10


class Mortal(Entity):
    def __init__(self, x, y, w, h, hp, health_bar_offset, name=None, current_animation=None, animation_spd=0):
        super().__init__(x, y, w, h, name, current_animation, animation_spd)
        self._hp = hp
        self._health_bar = Health_Bar(HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT, hp)
        self._health_bar_offset = health_bar_offset

    def get_hp(self):
        return self._hp

    def is_alive(self):
        return self._hp > 0

    def apply_damage(self, dmg):
        self._hp -= dmg
        if constants.SHOW_DEBUG:
            print(self._name + " is hit for " + str(dmg) + " damage! (" + str(self._hp) + " hp remaining)")

    def go(self, display):
        super().go(display)
        self._health_bar.draw(display, self, self._health_bar_offset)
