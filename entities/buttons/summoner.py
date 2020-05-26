import constants
from entities.buttons.button import Button


class Summoner(Button):
    def __init__(self, x, y, w, h, unit_id):
        self._unit_ID = unit_id
        if unit_id == constants.MACROPHAGE_SIDE:
            name = text_key = "macrophage_summoner"
        elif unit_id == constants.BACTERIOPHAGE_SIDE:
            name = text_key = "bacteriophage_summoner"
        else:
            raise ValueError("Wrong unit_id passed to Summoner.__init__().")
        super().__init__(x, y, w, h, name, text_key, None)
