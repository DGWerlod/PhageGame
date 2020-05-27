from entities.entity import Entity


class Microbe(Entity):
    def __init__(self, x, y, w, h, spd, hp, dmg, name=None, current_animation=None, animation_spd=0):
        super().__init__(x, y, w, h, name, current_animation, animation_spd)
        self._spd = spd
        self._hp = hp
        self._dmg = dmg
        self._in_front = None

    def is_alive(self):
        return self._hp > 0

    def attack(self, target):
        pass

    def apply_damage(self, dmg):
        self._hp -= dmg

    def set_in_front(self, in_front):
        self._in_front = in_front

    def pos(self):
        pass

    def go(self, display):
        super().go(display)
        self.pos()
