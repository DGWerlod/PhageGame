from entities.microbe import Microbe


class Macrophage(Microbe):
    def __init__(self, x, y, w, h, spd, hp, dmg, name=None):
        super().__init__(x, y, w, h, spd, hp, dmg, name)
