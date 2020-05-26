from entities.entity import Entity


class Button(Entity):
    def __init__(self, x, y, w, h, name=None, text_key=None, text_template=None):
        super().__init__(x, y, w, h, name)
        self.test_key = text_key
        self.text_template = text_template
