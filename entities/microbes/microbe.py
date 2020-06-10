from random import randint

import constants
import properties
from controls import keyboard
from entities.mortal import Mortal
from logic import collisions
from logic.rect import Rect

WALK_ANIMATION_KEY = "walk"
ATTACK_ANIMATION_KEY = "attack"
STATIC_ANIMATION_KEY = "static"

WALK_ANIMATION_SPEED = 5
ATTACK_ANIMATION_SPEED = 3
STATIC_ANIMATION_SPEED = 0  # No animation movement

HEALTH_BAR_OFFSET = 15
HEALTH_BAR_VARIANCE = 15


class Microbe(Mortal):
    def __init__(self, x, y, w, h, name=None, animation_spd=0, attack_key_frame=0):

        spd = properties.microbe_speeds[name]
        hp = properties.microbe_hit_points[name]
        dmg = properties.microbe_damages[name]

        # makes stacked health bars easier to see
        true_health_bar_offset = HEALTH_BAR_OFFSET + randint(0, HEALTH_BAR_VARIANCE)
        super().__init__(x, y, w, h, hp, true_health_bar_offset, name, WALK_ANIMATION_KEY, animation_spd)

        self._spd = spd
        self._dmg = dmg  # if damage is zero, throws projectiles instead
        self._attack_key_frame = attack_key_frame
        self._in_front = None
        self._cooldown_timer = 30
        self._cooldown_left = 0
        self._projectile_queued = False

    def set_in_front(self, in_front):
        self._in_front = in_front

    def speed_change_funtime(self):
        if keyboard.controls['held']['key_w'] and not keyboard.controls['held']['key_s']:
            self._animation_spd = max(1, self._animation_spd - 1)
        if keyboard.controls['held']['key_s'] and not keyboard.controls['held']['key_w']:
            self._animation_spd = min(15, self._animation_spd + 1)

    # subclasses that use projectiles MUST override this function
    def make_projectile(self):
        if self._dmg != 0:
            raise Exception("A microbe that doesn't throw projectiles cannot make one!")
        else:
            raise Exception("Microbe.make_projectile() was not overridden by projectile-throwing subclass.")

    # subclasses that use projectiles may override this function
    def get_range_rect(self):
        return Rect(self._x + self._w*(1 if self.get_allegiance() else -1), self._y, self._w*2, self._h)

    def check_projectile(self):
        if self._projectile_queued:
            self._projectile_queued = False
            return self.make_projectile()
        return None

    # subclasses MUST override this function
    def pos(self):
        raise Exception("Something isn't right - you shouldn't be seeing this message!")

    def go(self, display):

        super().go(display)

        self.speed_change_funtime()

        if self._current_animation == ATTACK_ANIMATION_KEY:
            if self._in_front and self._animation_cycle == self._attack_key_frame * self._animation_spd:
                if self._dmg != 0:
                    self._in_front.apply_damage(self._dmg)
                else:
                    self._projectile_queued = True
                if constants.SHOW_DEBUG:
                    print(self._name + " attacks!")
            elif self._animation_looped:
                self.change_animation(WALK_ANIMATION_KEY, WALK_ANIMATION_SPEED)

        target_rect = self._in_front.get_rect()
        if self._dmg and self._in_front and collisions.rectangles(self.get_rect(), target_rect) or \
           not self._dmg and self._in_front and collisions.rectangles(self.get_range_rect(), target_rect):
            if self._cooldown_left <= 0:
                self.change_animation(ATTACK_ANIMATION_KEY, ATTACK_ANIMATION_SPEED)
                self._cooldown_left = self._cooldown_timer
            elif self._current_animation == WALK_ANIMATION_KEY:
                self.change_animation(STATIC_ANIMATION_KEY, STATIC_ANIMATION_SPEED)
        else:
            if self._current_animation != WALK_ANIMATION_KEY:
                self.change_animation(WALK_ANIMATION_KEY, WALK_ANIMATION_SPEED)
            self.pos()

        if self._cooldown_left > 0:
            self._cooldown_left -= 1
