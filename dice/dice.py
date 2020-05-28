import random

class dice:
  def __init__(self, dicelength, dicelist, dicedic,):
    self.dicelength = dicelength # how many number the dice will have
    self.dicelist = range(0, self.dicelength, 1) # a list with all of the dice numbers
    self.dicedic = {1:"⚀", 2:"⚁", 3:"⚂", 4:"⚃", 5:"⚄", 6:"⚅"} # a nice way to display the results
  def roll(self):
    print("\nRolling...")
    num = random.ranint(1,self.dicelength,1)
    print("\n%s\nYou rolled a %s " % (self.dicedic[num], str(num)))
    return num
class critDice(dice):
  def __init__(self):
        dice.__init__(self, dicelength, dicelist, dicedic)
  def ifCrit(self):
    roll = dice.roll(self)
    if roll == 20:
      print("Critical hit!")
      return True
