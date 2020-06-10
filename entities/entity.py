from img.images import IMAGES
from logic.rect import Rect


class Entity(object):
    def __init__(self, x, y, w, h, name=None, current_animation=None, animation_spd=0, hitbox_offsets=(0, 0, 0, 0)):
        self._x = x
        self._y = y
        self._w = w
        self._h = h
        self._name = name
        self._current_animation = current_animation
        self._animation_spd = animation_spd   # the number of frames for which a single animation frame should be shown
        self._animation_cycle = 0  # current frame to be displayed is the floor of this value divided by _animation_spd
        self._animation_looped = False
        self._hitbox_offsets = hitbox_offsets  # (x, y, w, h)

    def get_rect(self):
        return Rect(self._x + self._hitbox_offsets[0], self._y + self._hitbox_offsets[1],
                    self._w + self._hitbox_offsets[2], self._h + self._hitbox_offsets[3])

    def get_name(self):
        return self._name

    # subclasses with an allegiance MUST override this function
    def get_allegiance(self):
        raise Exception("get_allegiance() called on non-allegiant Entity.")

    def change_animation(self, new_animation_key, new_animation_spd=None):
        self._current_animation = new_animation_key
        self._animation_cycle = 0
        self._animation_looped = False
        if new_animation_spd is not None:
            self._animation_spd = new_animation_spd

    def draw(self, display):
        if self._current_animation is None:
            raise ValueError("An entity cannot be missing a value for self._current_animation!")
        elif self._animation_spd == 0:
            now_image = IMAGES[self._name][self._current_animation][0]
        else:
            now_image = IMAGES[self._name][self._current_animation][self._animation_cycle // self._animation_spd]
        display.blit(now_image, (self._x, self._y))

    def go(self, display):
        num_frames = len(IMAGES[self._name][self._current_animation])
        if self._animation_spd != 0 and num_frames > 1:
            now_animation_cycle = self._animation_cycle + 1
            max_animation_cycle = num_frames * self._animation_spd
            if now_animation_cycle >= max_animation_cycle - 1:
                self._animation_looped = True
            self._animation_cycle = now_animation_cycle % max_animation_cycle
        self.draw(display)
