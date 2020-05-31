# FONTS
import pygame

pygame.font.init()

_source = "fonts/muli.ttf"
_sizes = [15, 20, 30, 70]
MULI = {}
for s in _sizes:
    MULI[str(s)] = pygame.font.Font(_source, s)

RENDERED_TEXT = {

}


def prepare_text(to_prepare):
    pass
