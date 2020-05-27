from img.images import IMAGES
from logic.rect import Rect


class Entity(object):
    def __init__(self, x, y, w, h, name=None, current_animation=None, animation_spd=0):
        self._x = x
        self._y = y
        self._w = w
        self._h = h
        self._name = name
        self._current_animation = current_animation
        self._animation_spd = animation_spd
        self._animation_cycle = 0

    def get_rect(self):
        return Rect(self._x, self._y, self._w, self._h)

    def draw(self, display):
        if self._current_animation is None:
            now_image = IMAGES[self._name]["active"][0]
        elif self._animation_spd == 0:
            raise ValueError("An entity cannot have an animation and an animation speed of zero.")
        else:
            now_image = IMAGES[self._name][self._current_animation][self._animation_cycle // self._animation_spd]
        display.blit(now_image, (self._x, self._y))

    def go(self, display):
        if self._current_animation is not None:
            self._animation_cycle = (self._animation_cycle + 1) % \
                                    (len(IMAGES[self._name][self._current_animation]) * self._animation_spd)
        self.draw(display)
