import constants
from entities.buttons.button import Button


class Summoner(Button):
    def __init__(self, x, y, w, h, unit_id):
        self._cooldown_timer = 30
        self._cooldown_left = 0
        self._unit_ID = unit_id
        if unit_id == constants.MACROPHAGE_SIDE:
            name = text_key = "macrophage_summoner"
        elif unit_id == constants.BACTERIOPHAGE_SIDE:
            name = text_key = "bacteriophage_summoner"
        else:
            raise ValueError("Wrong unit_id passed to Summoner.__init__().")
        super().__init__(x, y, w, h, name, text_key, None)

    def can_summon(self):
        if self._cooldown_left <= 0:
            return True
        else:
            return False

    def do_summon(self):
        if self.can_summon():
            self._cooldown_left = self._cooldown_timer
        else:
            raise AssertionError("Invalid summoning!")

    def go(self, display):

        if self.can_summon():
            self._current_animation = "active"
        else:
            self._current_animation = "inactive"
        
        super().go(display)

        self._cooldown_left = max(0, self._cooldown_left - 1)


