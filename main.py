import pygame
from pygame.locals import *

import constants
from fonts import text
from sound import sounds
from controls import keyboard, mouse
# from dice.dice import Dice, Crit_Dice

from levels.level_builder import build_level

flags = DOUBLEBUF

pygame.init()

window = pygame.display.set_mode((constants.GAME_WIDTH, constants.GAME_HEIGHT), flags)
window.set_alpha(None)
pygame.display.set_caption("PhageGame")
pygame.mouse.set_cursor(*pygame.cursors.diamond)
clock = pygame.time.Clock()


def listen():
    keyboard.new_frame()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == sounds.END_FLAG:
            sounds.change_music(sounds.overture_loop_time)
        else:
            keyboard.listen(event)
    mouse.listen()
    return True


def draw_debug_visuals():
    pygame.draw.line(window, constants.BLACK, (0, constants.HUD_TOP_END_Y),
                     (constants.GAME_WIDTH, constants.HUD_TOP_END_Y), 3)
    pygame.draw.line(window, constants.BLACK, (0, constants.HUD_BOTTOM_Y),
                     (constants.GAME_WIDTH, constants.HUD_BOTTOM_Y), 3)
    pygame.draw.line(window, constants.YELLOW, (constants.GAME_WIDTH // 2, 0),
                     (constants.GAME_WIDTH // 2, constants.GAME_HEIGHT), 3)
    pygame.draw.rect(window, constants.MAGENTA,
                     pygame.Rect(constants.GAME_WIDTH // 2 - 50, constants.GAME_HEIGHT // 2, 100, 125))


def main():

    running = True
    game_state = constants.AUTHORS
    current_level = None

    # sounds.start_music()

    while running:

        if game_state == constants.AUTHORS:

            window.fill(constants.BLACK)
            for t in text.STATE_AUTHORS_TEXT:
                window.blit(text.RENDERED_TEXT[t][0], text.RENDERED_TEXT[t][1])
            if keyboard.controls['pressed']['key_enter']:
                game_state = constants.SPLASH
            elif pygame.mixer.music.get_pos() > sounds.splash_shift_time * 1000:
                game_state = constants.SPLASH

        elif game_state == constants.SPLASH:

            window.fill(constants.BLACK)
            for t in text.STATE_SPLASH_TEXT:
                window.blit(text.RENDERED_TEXT[t][0], text.RENDERED_TEXT[t][1])
            if keyboard.controls['pressed']['key_enter']:
                game_state = constants.LEVEL_SELECT

        elif game_state == constants.LEVEL_SELECT:

            # to be fleshed out in the future
            current_level = build_level(1)
            game_state = constants.GAMEPLAY

        elif game_state == constants.UPGRADES:

            pass

        elif game_state == constants.GAMEPLAY:
            current_level.go(window)
            if constants.SHOW_DEBUG:
                draw_debug_visuals()

        elif game_state == constants.PAUSE:

            pass

        elif game_state == constants.VICTORY:

            pass

        elif game_state == constants.DEFEAT:

            pass

        else:
            raise ValueError("Invalid game state!")

        # Debug
        fps = text.MULI[15].render(str(round(clock.get_fps(), 1)), True, constants.WHITE)
        window.blit(fps, (constants.GAME_WIDTH - 40, 5))

        # Update Window
        pygame.display.update()
        clock.tick(30)

        running = listen()

    pygame.quit()


main()
