from random import randint

import constants
from controls import keyboard
from entities.mortal import Mortal
from logic import collisions

WALK_ANIMATION_KEY = "walk"
ATTACK_ANIMATION_KEY = "attack"

WALK_ANIMATION_SPEED = 5
ATTACK_ANIMATION_SPEED = 3

HEALTH_BAR_OFFSET = 15
HEALTH_BAR_VARIANCE = 15


class Microbe(Mortal):
    def __init__(self, x, y, w, h, spd, hp, dmg, name=None, animation_spd=0, attack_key_frame=0):
        # makes stacked health bars easier to see
        true_health_bar_offset = HEALTH_BAR_OFFSET + randint(0, HEALTH_BAR_VARIANCE)
        super().__init__(x, y, w, h, hp, true_health_bar_offset, name, WALK_ANIMATION_KEY, animation_spd)
        self._spd = spd
        self._dmg = dmg
        self._attack_key_frame = attack_key_frame
        self._in_front = None
        self._cooldown_timer = 30
        self._cooldown_left = 0

    def get_unit_id(self):
        return self._name

    def set_in_front(self, in_front):
        self._in_front = in_front

    def speed_change_funtime(self):
        if keyboard.controls['held']['key_w'] and not keyboard.controls['held']['key_s']:
            self._animation_spd = max(1, self._animation_spd - 1)
        if keyboard.controls['held']['key_s'] and not keyboard.controls['held']['key_w']:
            self._animation_spd = min(15, self._animation_spd + 1)

    # subclasses MUST override this function
    def pos(self):
        raise Exception("Something isn't right - you shouldn't be seeing this message!")

    def go(self, display):

        super().go(display)

        self.speed_change_funtime()

        if self._current_animation == ATTACK_ANIMATION_KEY:
            if self._in_front and self._animation_cycle == self._attack_key_frame * self._animation_spd:
                self._in_front.apply_damage(self._dmg)
                if constants.SHOW_DEBUG:
                    # noinspection PyProtectedMember
                    print(self._name + " attacks " + self._in_front._name + " for " + str(self._dmg) +
                          " damage! (" + str(self._in_front._hp) + " hp remaining)")
            elif self._animation_looped:
                self.change_animation(WALK_ANIMATION_KEY, WALK_ANIMATION_SPEED)

        if self._in_front and collisions.rectangles(self.get_rect(), self._in_front.get_rect()):
            if self._cooldown_left <= 0:
                self.change_animation(ATTACK_ANIMATION_KEY, ATTACK_ANIMATION_SPEED)
                self._cooldown_left = self._cooldown_timer
        else:
            self.pos()

        if self._cooldown_left > 0:
            self._cooldown_left -= 1
