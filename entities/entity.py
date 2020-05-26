from img.images import IMAGES
from logic.rect import Rect


class Entity(object):
    def __init__(self, x, y, w, h, name=None):
        self._x = x
        self._y = y
        self._w = w
        self._h = h
        self._name = name

    def get_rect(self):
        return Rect(self._x, self._y, self._w, self._h)

    def draw(self, display):
        display.blit(IMAGES[self._name], (self._x, self._y))

    def go(self, display):
        self.draw(display)
