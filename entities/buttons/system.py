from entities.buttons.button import Button

VALID_TYPES = {
    "action": ["pause", "play"],
    "music": ["audible", "muted"],
    "back": ["back"],
    "mode": ["ai", "pvp"]
}


class System(Button):
    def __init__(self, x, y, w, h, action_type, current_state=0):
        if action_type not in VALID_TYPES:
            raise ValueError("Invalid name passed to System.__init__().")
        self._action_type = action_type
        self._current_state = current_state
        super().__init__(x, y, w, h, action_type, VALID_TYPES[action_type][current_state])

    def get_state(self):
        return VALID_TYPES[self._action_type][self._current_state]

    def change_state(self):
        if self._action_type == "back":
            raise AssertionError("Can't change state of back button!")
        else:
            if self._current_state == 0:
                self._current_state = 1
            elif self._current_state == 1:
                self._current_state = 0
            else:
                raise ValueError("Something went wrong; invalid current_state")
            self.change_animation(VALID_TYPES[self._action_type][self._current_state])
