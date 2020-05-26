from logic.rect import Rect


class Entity(object):
    def __init__(self, x, y, w, h, name=None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.name = name

    def get_rect(self):
        return Rect(self.x, self.y, self.w, self.h)

    def draw(self, display):
        pass

    def go(self, display):
        self.draw(display)
