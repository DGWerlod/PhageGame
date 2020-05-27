from entities.microbe import Microbe


class Macrophage(Microbe):
    def __init__(self, x, y, w, h, spd, hp, dmg, name=None, current_animation=None, animation_spd=0):
        super().__init__(x, y, w, h, spd, hp, dmg, name, current_animation, animation_spd)
