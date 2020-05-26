from entities.buttons.button import Button


class System(Button):
    def __init__(self, x, y, w, h, name=None, text_key=None, text_template=None):
        super().__init__(x, y, w, h, name, text_key, text_template)
