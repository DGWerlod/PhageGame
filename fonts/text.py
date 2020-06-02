# FONTS
import pygame

import constants

pygame.font.init()

_source = "fonts/muli.ttf"
_sizes = [15, 20, 30, 70]
MULI = {}
for s in _sizes:
    MULI[s] = pygame.font.Font(_source, s)

_created_by = MULI[70].render("Created by", True, constants.WHITE)
_authors = MULI[30].render("Daniel DeAnda | Desmond Kamas | Kaweees", True, constants.WHITE)
_created_with = MULI[70].render("Created with", True, constants.WHITE)
_tools = MULI[30].render("Python | Pygame | PyInstaller | Pycharm | VS Code | GitHub | Love", True, constants.WHITE)
_begin = MULI[30].render("Press Enter", True, constants.GREY)

_splash_dummy = MULI[70].render("Splash Screen Goes Here", True, constants.WHITE)

RENDERED_TEXT = {
    "created_by": (_created_by, _created_by.get_rect(centerx=constants.CENTER_X, top=constants.CENTER_Y - 160)),
    "authors": (_authors, _authors.get_rect(centerx=constants.CENTER_X, top=constants.CENTER_Y - 70)),
    "created_with": (_created_with, _created_with.get_rect(centerx=constants.CENTER_X, top=constants.CENTER_Y - 10)),
    "tools": (_tools, _tools.get_rect(centerx=constants.CENTER_X, top=constants.CENTER_Y + 80)),
    "begin": (_begin, _begin.get_rect(right=constants.GAME_WIDTH - 20, bottom=constants.GAME_HEIGHT - 15)),
    "splash_dummy": (_splash_dummy, _splash_dummy.get_rect(centerx=constants.CENTER_X, centery=constants.CENTER_Y))
}

STATE_AUTHORS_TEXT = {"created_by", "authors", "created_with", "tools", "begin"}
STATE_SPLASH_TEXT = {"splash_dummy", "begin"}
