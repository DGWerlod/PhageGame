from entities.buttons.button import Button


class Summoner(Button):
    def __init__(self, x, y, w, h, unit_id):
        self._cooldown_timer = 30
        self._cooldown_left = 0
        self._unit_ID = unit_id
        name = unit_id + "_summoner"
        super().__init__(x, y, w, h, name)

    def get_unit_id(self):
        return self._unit_ID

    def can_summon(self):
        return self._cooldown_left <= 0

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
