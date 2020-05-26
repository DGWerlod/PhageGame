from entities.entity import Entity


class Microbe(Entity):
    def __init__(self, x, y, w, h, spd, hp, dmg, name=None):
        super().__init__(x, y, w, h, name)
        self.spd = spd
        self.hp = hp
        self.dmg = dmg

    def is_alive(self):
        return self.hp > 0

    def attack(self, target):
        pass

    def apply_damage(self, dmg):
        self.hp -= dmg

    def pos(self):
        pass

    def go(self, display):
        self.draw(display)
        self.pos()
