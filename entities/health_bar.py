import pygame
from pygame.rect import Rect

import constants


class Health_Bar(object):
    def __init__(self, w, h, max_hp):
        self._w = w
        self._h = h
        self._max_hp = max_hp

    def draw(self, display, parent, vert_offset):
        parent_rect = parent.get_rect()
        bar_x = parent_rect.X + parent_rect.W // 2 - self._w // 2
        pygame.draw.rect(display, constants.RED, Rect(bar_x, parent_rect.Y - vert_offset, self._w, self._h))
        width_remaining = int(parent.get_hp() / self._max_hp * self._w)
        pygame.draw.rect(display, constants.GREEN, Rect(bar_x, parent_rect.Y - vert_offset, width_remaining, self._h))

        # debug drawing for hit boxes
        pygame.draw.rect(display, constants.BLACK, Rect(parent_rect.X, parent_rect.Y, parent_rect.W, parent_rect.H), 1)
        center_x = parent_rect.X + parent_rect.W/2
        pygame.draw.line(display, constants.BLACK, (center_x, parent_rect.Y), (center_x, parent_rect.Y + parent_rect.H))
