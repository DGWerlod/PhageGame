import pygame
from pygame.locals import *

import constants
from entities.buttons.level_selector import Level_Selector
from entities.buttons.system import System
from fonts import text
from logic import graphics, collisions
from sound import sounds
from controls import keyboard, mouse
# from dice.dice import Dice, Crit_Dice

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

    if constants.SHOW_DEBUG:
        music_start = 1
    else:
        music_start = 0
    back_button = System(0, 0, 125, 125, "back")
    music_button = System(125, 0, 125, 125, "music", music_start)
    action_button = System(constants.GAME_WIDTH - 125, 0, 125, 125, "action")

    selectors = []
    x_location = 5
    y_location = constants.HUD_HEIGHT + 5
    selector_width = 160
    selector_height = 110
    for num in range(1, constants.NUM_LEVELS + 1):
        selectors.append(Level_Selector(x_location, y_location, selector_width, selector_height, num))
        x_location += selector_width + 5
        if x_location + selector_width > constants.GAME_WIDTH:
            x_location = 5
            y_location += selector_height + 5

    running = True
    game_state = constants.AUTHORS
    current_level = None

    if not constants.SHOW_DEBUG:
        sounds.start_music()

    while running:

        window.fill(constants.GREY)

        # Process according to game_state

        if game_state == constants.AUTHORS:

            graphics.fill_game_rect(window, constants.BLACK)
            for t in text.STATE_AUTHORS_TEXT:
                window.blit(text.RENDERED_TEXT[t][0], text.RENDERED_TEXT[t][1])
            if keyboard.controls['pressed']['key_enter']:
                game_state = constants.SPLASH
            elif pygame.mixer.music.get_pos() > sounds.splash_shift_time * 1000:
                game_state = constants.SPLASH

        elif game_state == constants.SPLASH:

            graphics.fill_game_rect(window, constants.BLACK)
            for t in text.STATE_SPLASH_TEXT:
                window.blit(text.RENDERED_TEXT[t][0], text.RENDERED_TEXT[t][1])
            if keyboard.controls['pressed']['key_enter']:
                game_state = constants.LEVEL_SELECT

        elif game_state == constants.LEVEL_SELECT:

            graphics.fill_game_rect(window, constants.BLACK)
            for s in selectors:
                s.go(window)
                if mouse.controls['click'] and collisions.rect_point(s.get_rect(), mouse.controls['pos']):
                    current_level = s.get_target()
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

        # Handle system buttons

        if game_state > constants.SPLASH:

            if game_state != constants.PAUSE:
                music_button.go(window)
                if mouse.controls['click'] and collisions.rect_point(music_button.get_rect(), mouse.controls['pos']):
                    if music_button.get_state() == "audible":
                        sounds.stop_music()
                    else:  # music_button.get_state() == "muted"
                        sounds.start_music()
                    music_button.change_state()

            if game_state < constants.PAUSE:

                back_button.go(window)
                if mouse.controls['click'] and collisions.rect_point(back_button.get_rect(), mouse.controls['pos']):
                    if game_state == constants.GAMEPLAY:
                        game_state -= 2
                    else:
                        game_state -= 1

            if game_state == constants.GAMEPLAY or game_state == constants.PAUSE:

                action_button.go(window)
                if mouse.controls['click'] and collisions.rect_point(action_button.get_rect(), mouse.controls['pos']):
                    if action_button.get_state() == "pause":
                        game_state = constants.PAUSE
                    else:  # action_button.get_state() == "play"
                        game_state = constants.GAMEPLAY
                    action_button.change_state()

        if constants.SHOW_DEBUG:
            fps = text.MULI[15].render(str(round(clock.get_fps(), 1)), True, constants.WHITE)
            window.blit(fps, (constants.GAME_WIDTH - 40, 5))

        # Update Window
        pygame.display.update()
        clock.tick(30)

        running = listen()

    pygame.quit()


main()
