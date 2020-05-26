from entities.entity import Entity


class HUD(Entity):
    def __init__(self, x, y, w, h, name=None):
        super().__init__(x, y, w, h, name)
