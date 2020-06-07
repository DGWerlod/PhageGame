import pygame
from pygame.rect import Rect
from pygame import Surface
import constants
from entities.buttons.button import Button
from entities.microbes.microbe_builder import build_microbe

class Summoner(Button):

    def __init__(self, x, y, w, h, unit_id):
        self._cooldown_timer = max(30, build_microbe(unit_id).get_hp() // 3)
        self._cooldown_left = 0
        self._unit_ID = unit_id
        self._current_animation = "active"
        name = unit_id + "_summoner"
        super().__init__(x, y, w, h, name)

    def get_name(self):
        return self._unit_ID

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
        display.blit(shade, (self._x, self._y + (self._h * (self._cooldown_timer - self._cooldown_left) // self._cooldown_timer)))
        
        pygame.draw.rect(display, constants.BLACK, Rect(self._x, self._y, self._w, self._h), 2)

        self._cooldown_left = max(0, self._cooldown_left - 1)
