from entities.entity import Entity


class Mortal(Entity):
    def __init__(self, x, y, w, h, hp, name=None, current_animation=None, animation_spd=0):
        super().__init__(x, y, w, h, name, current_animation, animation_spd)
        self._hp = hp

    def is_alive(self):
        return self._hp > 0

    def apply_damage(self, dmg):
        self._hp -= dmg
