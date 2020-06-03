from entities.entity import Entity
from entities.health_bar import Health_Bar


class Mortal(Entity):
    def __init__(self, x, y, w, h, hp, health_bar_height, name=None, current_animation=None, animation_spd=0):
        super().__init__(x, y, w, h, name, current_animation, animation_spd)
        self._hp = hp
        self._health_bar = Health_Bar(50, 5, hp)
        self._health_bar_height = health_bar_height

    def get_hp(self):
        return self._hp

    def is_alive(self):
        return self._hp > 0

    def apply_damage(self, dmg):
        self._hp -= dmg

    def go(self, display):
        super().go(display)
        self._health_bar.draw(display, self, self._health_bar_height)
