import random
import constants


class Die(object):
    def __init__(self, sides=6):
        self.sides = sides  # how many number the dice will have
        self.list = range(0, self.sides, 1)  # a list with all of the dice numbers

    def roll(self):
        # print("Rolling...")
        num = random.randint(1, self.sides)
        # if constants.SHOW_DEBUG:
        #     print("You rolled a %s" % (str(num)))
        return num


class D20(Die):
    def __init__(self):
        super().__init__(20)

    def if_crit(self):
        roll = super().roll()
        if roll == 20:
            if constants.SHOW_DEBUG:
                print("Critical hit!")
            return True
        else:
            return False
