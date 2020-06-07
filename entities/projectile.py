import constants
from entities.entity import Entity
from logic import collisions


class Projectile(Entity):
    def __init__(self, x, y, w, h, spd, dmg, source):
        super().__init__(x, y, w, h, source.get_name() + "_projectile", "fly")
        self._spd = spd
        self._dmg = dmg
        self._source = source
        self._in_front = None
        self._active = True

    def get_allegiance(self):
        return self._source.get_allegiance()

    def is_active(self):
        return self._active

    def set_in_front(self, in_front):
        self._in_front = in_front

    def pos(self):
        if self._source.get_allegiance() == constants.MACROPHAGE_SIDE:
            self._x += self._spd
        elif self._source.get_allegiance() == constants.BACTERIOPHAGE_SIDE:
            self._x -= self._spd
        else:
            raise ValueError("Wrong allegiance passed to Projectile.__init__().")

    def go(self, display):
        self.pos()
        super().go(display)
        if self._in_front and collisions.rectangles(self.get_rect(), self._in_front.get_rect()):
            self._in_front.apply_damage(self._dmg)
            self._active = False
