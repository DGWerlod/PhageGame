import pygame
from pygame.rect import Rect
from pygame import Surface

import constants
import properties
from entities.buttons.button import Button


class Summoner(Button):

    def __init__(self, x, y, w, h, unit_name):
        super().__init__(x, y, w, h, unit_name + "_summoner")
        self._unit_name = unit_name
        self._cooldown_timer = properties.summoner_cooldowns[unit_name]
        self._cooldown_left = 0

    def get_unit_name(self):
        return self._unit_name

    def can_summon(self):
        return self._cooldown_left <= 0

    def do_summon(self):
        if self.can_summon():
            self._cooldown_left = self._cooldown_timer
        else:
            raise AssertionError("Invalid summoning!")

    def go(self, display):

        super().go(display)

        shade = Surface((self._w, self._h * self._cooldown_left // self._cooldown_timer))
        shade.set_alpha(63)
        shade.fill(constants.BLACK)
        y_pos = self._y + (self._h * (self._cooldown_timer - self._cooldown_left) // self._cooldown_timer)
        display.blit(shade, (self._x, y_pos))

        pygame.draw.rect(display, constants.BLACK, Rect(self._x, self._y, self._w, self._h), 2)

        self._cooldown_left = max(0, self._cooldown_left - 1)
