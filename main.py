import pygame
from pygame.locals import *

import constants
from entities.hud import HUD
from fonts import text
from img.images import IMAGES
from logic import graphics
from sound import sounds
from controls import keyboard, mouse

flags = DOUBLEBUF

pygame.init()

window = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT), flags)
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


def draw_hud_dividing_lines():
    pygame.draw.line(window, constants.BLACK, (0, constants.HUD_HEIGHT),
                     (constants.GAME_WIDTH, constants.HUD_HEIGHT), 3)
    pygame.draw.line(window, constants.BLACK, (0, constants.BOTTOM_HUD),
                     (constants.GAME_WIDTH, constants.BOTTOM_HUD), 3)


def draw_debug_visuals():
    pygame.draw.line(window, constants.YELLOW, (constants.CENTER_X, constants.HUD_HEIGHT),
                     (constants.CENTER_X, constants.HUD_HEIGHT + constants.GAME_HEIGHT), 3)
    pygame.draw.rect(window, constants.MAGENTA,
                     pygame.Rect(constants.CENTER_X - 50, constants.CENTER_Y, 100, 125))


def main():

    running = True
    game_state = constants.AUTHORS
    current_level = None
    hud = HUD()

    if not constants.SHOW_DEBUG:
        sounds.start_music()

    while running:

        if keyboard.controls['pressed']['key_escape']:
            constants.SHOW_DEBUG = not constants.SHOW_DEBUG

        window.fill(constants.GREY)

        if game_state == constants.AUTHORS:

            graphics.fill_game_rect(window, constants.BLACK)
            for t in text.STATE_AUTHORS_TEXT:
                window.blit(text.RENDERED_TEXT[t][0], text.RENDERED_TEXT[t][1])
            if keyboard.controls['pressed']['key_enter']:
                game_state = constants.SPLASH
            elif pygame.mixer.music.get_pos() > sounds.splash_shift_time * 1000:
                game_state = constants.SPLASH

        elif game_state == constants.SPLASH:

            window.blit(IMAGES["splash"]["splash"][0], (0, 0))

            # graphics.fill_game_rect(window, constants.BLACK)
            # for t in text.STATE_SPLASH_TEXT:
            #     window.blit(text.RENDERED_TEXT[t][0], text.RENDERED_TEXT[t][1])
            
            if keyboard.controls['pressed']['key_enter']:
                game_state = constants.LEVEL_SELECT

        elif game_state == constants.LEVEL_SELECT:

            graphics.fill_game_rect(window, constants.BLACK)
            new_level = hud.handle_selectors(window)
            if new_level is not None:
                current_level = new_level
                game_state = constants.GAMEPLAY

        elif game_state == constants.UPGRADES:

            pass

        elif game_state == constants.GAMEPLAY:

            current_level.go(window)
            draw_hud_dividing_lines()
            if constants.SHOW_DEBUG:
                draw_debug_visuals()

            win_state = current_level.check_winner()
            if win_state > 0:
                game_state = constants.VICTORY
            elif win_state < 0:
                game_state = constants.DEFEAT

        elif game_state == constants.PAUSE:

            graphics.fill_game_rect(window, constants.BLACK)
            window.blit(text.RENDERED_TEXT["paused"][0], text.RENDERED_TEXT["paused"][1])

        elif game_state == constants.VICTORY:

            graphics.fill_game_rect(window, constants.BLACK)
            window.blit(text.RENDERED_TEXT["victory"][0], text.RENDERED_TEXT["victory"][1])
            window.blit(text.RENDERED_TEXT["continue"][0], text.RENDERED_TEXT["continue"][1])
            if keyboard.controls['pressed']['key_enter']:
                game_state = constants.LEVEL_SELECT

        elif game_state == constants.DEFEAT:

            graphics.fill_game_rect(window, constants.BLACK)
            window.blit(text.RENDERED_TEXT["defeat"][0], text.RENDERED_TEXT["defeat"][1])
            window.blit(text.RENDERED_TEXT["continue"][0], text.RENDERED_TEXT["continue"][1])
            if keyboard.controls['pressed']['key_enter']:
                game_state = constants.LEVEL_SELECT

        else:
            raise ValueError("Invalid game state!")

        game_state = hud.handle_system_buttons(window, game_state)

        if constants.SHOW_DEBUG:
            fps = text.MULI[15].render(str(round(clock.get_fps(), 1)), True, constants.WHITE)
            window.blit(fps, (constants.GAME_WIDTH - 40, 5))

        # Update Window
        pygame.display.update()
        clock.tick(30)

        running = listen()

    pygame.quit()


main()
