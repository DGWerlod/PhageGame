import constants
from controls import mouse
from entities.buttons.level_selector import Level_Selector
from entities.buttons.system import System
from logic import collisions
from sound import sounds

LEVEL_SELECTOR_WIDTH = 160
LEVEL_SELECTOR_HEIGHT = 110


class HUD(object):
    def __init__(self):

        if constants.SHOW_DEBUG:
            music_start = 1
        else:
            music_start = 0
        self._back_button = System(0, 0, 125, 125, "back")
        self._music_button = System(125, 0, 125, 125, "music", music_start)
        self._action_button = System(constants.GAME_WIDTH - 125, 0, 125, 125, "action")

        self._selectors = []
        x_loc = 5
        y_loc = constants.HUD_HEIGHT + 5
        for num in range(1, constants.NUM_LEVELS + 1):
            self._selectors.append(Level_Selector(x_loc, y_loc, LEVEL_SELECTOR_WIDTH, LEVEL_SELECTOR_HEIGHT, num))
            x_loc += LEVEL_SELECTOR_WIDTH + 5
            if x_loc + LEVEL_SELECTOR_WIDTH > constants.GAME_WIDTH:
                x_loc = 5
                y_loc += LEVEL_SELECTOR_HEIGHT + 5

    def handle_selectors(self, window):
        for s in self._selectors:
            s.go(window)
            if mouse.controls['click'] and collisions.rect_point(s.get_rect(), mouse.controls['pos']):
                return s.get_target()
        return None

    def handle_system_buttons(self, window, game_state):

        if game_state > constants.SPLASH:

            if game_state != constants.PAUSE:
                self._music_button.go(window)
                if mouse.controls['click']:
                    if collisions.rect_point(self._music_button.get_rect(), mouse.controls['pos']):
                        if self._music_button.get_state() == "audible":
                            sounds.stop_music()
                        else:  # music_button.get_state() == "muted"
                            sounds.start_music()
                        self._music_button.change_state()

            if game_state < constants.PAUSE:

                self._back_button.go(window)
                if mouse.controls['click']:
                    if collisions.rect_point(self._back_button.get_rect(), mouse.controls['pos']):
                        if game_state == constants.GAMEPLAY:
                            game_state -= 2
                        else:
                            game_state -= 1

            if game_state == constants.GAMEPLAY or game_state == constants.PAUSE:

                self._action_button.go(window)
                if mouse.controls['click']:
                    if collisions.rect_point(self._action_button.get_rect(), mouse.controls['pos']):
                        if self._action_button.get_state() == "pause":
                            game_state = constants.PAUSE
                        else:  # action_button.get_state() == "play"
                            game_state = constants.GAMEPLAY
                        self._action_button.change_state()

        return game_state
