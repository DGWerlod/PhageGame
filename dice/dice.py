import random


class Dice(object):
    def __init__(self, dicelength, dicelist, dicedic):
        self.dicelength = dicelength  # how many number the dice will have
        self.dicelist = range(0, self.dicelength, 1)  # a list with all of the dice numbers
        self.dicedic = {1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"}  # a nice way to display the results

    def roll(self):
        print("\nRolling...")
        num = random.randint(1, self.dicelength, 1)
        print("\n%s\nYou rolled a %s " % (self.dicedic[num], str(num)))
        return num


class Crit_Dice(Dice):
    def __init__(self, dicelength, dicelist, dicedic):
        super().__init__(dicelength, dicelist, dicedic)

    def if_crit(self):
        roll = super().roll()
        if roll == 20:
            print("Critical hit!")
            return True
