import random
import constants


class Dice(object):
    def __init__(self, dicelength=6, dicedic=None):
        self.dicelength = dicelength  # how many number the dice will have
        self.dicelist = range(0, self.dicelength, 1)  # a list with all of the dice numbers
        self.dicedic = dicedic if dicedic else {1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"}  # a nice way to display the results

    def roll(self):
        # print("\nRolling...")
        num = random.randint(1, self.dicelength)
        if constants.SHOW_DEBUG:
            print("\n%s\nYou rolled a %s " % (self.dicedic[num], str(num)))
        return num


class Crit_Dice(Dice):
    def __init__(self):
        super().__init__(20, {x : str(x) for x in range(1,21)})

    def if_crit(self):
        roll = super().roll()
        if roll == 20:
            print("Critical hit!")
            return True
