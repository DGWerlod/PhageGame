import pygame
from pygame.rect import Rect

import constants
from logic import graphics


class Health_Bar(object):
    def __init__(self, w, h, max_hp):
        self._w = w
        self._h = h
        self._max_hp = max_hp

    def draw(self, display, parent, vert_offset):
        parent_rect = parent.get_rect()
        bar_x = parent_rect.X + parent_rect.W // 2 - self._w // 2
        full_rect = Rect(bar_x, parent_rect.Y - vert_offset, self._w, self._h)
        width_remaining = int(parent.get_hp() / self._max_hp * self._w)
        if width_remaining < self._h:  # Ensures that rounded_rect...
            width_remaining = self._h  # never draws bad visuals
        partial_rect = Rect(bar_x, parent_rect.Y - vert_offset, width_remaining, self._h)

        # pygame.draw.rect(display, constants.RED, full_rect)
        # pygame.draw.rect(display, constants.GREEN, partial_rect)
        graphics.aa_round_rect(display, full_rect, constants.BLACK, self._h // 3, 1, constants.RED)
        graphics.aa_round_rect(display, partial_rect, constants.BLACK, self._h // 3, 1, constants.GREEN)

        # debug drawing for hit boxes
        if constants.SHOW_DEBUG:
            pygame.draw.rect(display, constants.BLACK,
                             Rect(parent_rect.X, parent_rect.Y, parent_rect.W, parent_rect.H), 1)
            center_x = parent_rect.X + parent_rect.W/2
            pygame.draw.line(display, constants.BLACK,
                             (center_x, parent_rect.Y), (center_x, parent_rect.Y + parent_rect.H))
