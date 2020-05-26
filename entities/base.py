from entities.entity import Entity


class Base(Entity):
    def __init__(self, x, y, w, h, hp, name=None):
        super().__init__(x, y, w, h, name)
        self._hp = hp
