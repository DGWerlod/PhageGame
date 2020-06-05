from entities.entity import Entity


class Button(Entity):
    def __init__(self, x, y, w, h, name=None, current_animation="active"):
        super().__init__(x, y, w, h, name, current_animation)
