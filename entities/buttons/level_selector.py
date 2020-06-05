import pygame
from pygame.rect import Rect

import constants
from entities.buttons.button import Button
from fonts.text import MULI

from levels.level_builder import build_level


class Level_Selector(Button):
    def __init__(self, x, y, w, h, target_level_number):
        string_target = str(target_level_number)
        super().__init__(x, y, w, h, "level_selector_" + string_target)
        self._target_level_number = target_level_number
        text = MULI[20].render("Level " + string_target, True, constants.WHITE)
        self._text = (text, text.get_rect(centerx=x+w/2, centery=y+h/2))
        self._pygame_rect = Rect(x, y, w, h)

    def get_target(self):
        return build_level(self._target_level_number)

    def go(self, display):
        pygame.draw.rect(display, constants.GREY, self._pygame_rect)
        display.blit(self._text[0], self._text[1])
