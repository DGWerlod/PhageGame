from entities.entity import Entity
from logic import collisions


class Microbe(Entity):
    def __init__(self, x, y, w, h, spd, hp, dmg, name=None, current_animation=None, animation_spd=0):
        super().__init__(x, y, w, h, name, current_animation, animation_spd)
        self._spd = spd
        self._hp = hp
        self._dmg = dmg
        self._in_front = None
        self._cooldown_timer = 30
        self._cooldown_left = 0

    def is_alive(self):
        return self._hp > 0

    def apply_damage(self, dmg):
        self._hp -= dmg

    def set_in_front(self, in_front):
        self._in_front = in_front

    # subclasses MUST override this function
    def pos(self):
        raise Exception("Something isn't right - you shouldn't be seeing this message!")

    def go(self, display):
        super().go(display)
        if self._in_front and collisions.rectangles(self.get_rect(), self._in_front.get_rect()):
            if self._cooldown_left <= 2:
                if self._current_animation != "attack":
                    self._walk_spd = self._animation_spd
                self._current_animation = "attack"
                self._animation_spd = 1
            if self._cooldown_left <= 0:
                self._in_front.apply_damage(self._dmg)
                # debug printing
                # noinspection PyProtectedMember
                print(self._name + " attacks " + self._in_front._name + " for " + str(self._dmg) + " damage! " +
                      "(" + str(self._in_front._hp) + " hp remaining)")
                self._cooldown_left = self._cooldown_timer
        else:
            self.pos()
            if self._current_animation != "walk":
                self._current_animation = "walk"
                self._animation_spd = self._walk_spd
        if self._cooldown_left > 0:
            self._cooldown_left -= 1
