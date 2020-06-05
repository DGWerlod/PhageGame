# GENERAL VARIABLES
HUD_HEIGHT = 125
GAME_WIDTH, GAME_HEIGHT = 1200, 500
WINDOW_WIDTH, WINDOW_HEIGHT = GAME_WIDTH, GAME_HEIGHT + HUD_HEIGHT * 2
CENTER_X, CENTER_Y = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2
BOTTOM_HUD = WINDOW_HEIGHT - HUD_HEIGHT

# COLORS
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)

# SIDES
LEFT = MACROPHAGE_SIDE = True
RIGHT = BACTERIOPHAGE_SIDE = False

# STATES
AUTHORS = 0
SPLASH = 1
LEVEL_SELECT = 2
UPGRADES = 3
GAMEPLAY = 4
PAUSE = 5
VICTORY = 6
DEFEAT = 7

# LEVEL INFO
NUM_LEVELS = 1  # natural maximum is 28

# UNIT IDS
M_BASIC = "macrophoot"
B_BASIC = "buffteriophage"
B_TANK = "tankphage"

# DEBUG
SHOW_DEBUG = True
