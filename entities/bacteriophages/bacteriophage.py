from entities.microbe import Microbe
import pygame.surface
from img.images import IMAGES


class Bacteriophage(Microbe):
    def __init__(self, x, y, w, h, spd, hp, dmg, name=None):
        super().__init__(x, y, w, h, spd, hp, dmg, name)
        self._cycle = 0

    def go(self, context, in_front):
        self._cycle = (self._cycle + 1) % (8*self._spd)
        context.blit(IMAGES[self._name]["walk"][self._cycle // self._spd], (self._x, self._y)) 
