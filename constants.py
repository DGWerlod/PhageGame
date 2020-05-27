import pygame

pygame.font.init()

# GENERAL VARIABLES
GAME_WIDTH, GAME_HEIGHT = 900, 600

# COLORS
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# FONTS
SOURCE, SIZES = "fonts/muli.ttf", [15, 20, 30, 70]
MULI = {}
for s in SIZES:
    MULI[str(s)] = pygame.font.Font(SOURCE, s)

# SIDES
LEFT, MACROPHAGE_SIDE = True, True
RIGHT, BACTERIOPHAGE_SIDE = False, False
