import random

class Dice:
    def __init__(self, sides=6):
        self.sides = sides
    # adding sides as a variable to the dice

    def roll(self):
        return random.randint(1, self.sides)
#     randint is just random integer


# dice = Dice(15)
# for roll in range(100):
#     print(dice.roll())
# putting the number of sides on the dice and rolling

dice2 = Dice()
# you can also set a default number of sides
# and then leave this parentheses blank
print(dice2.roll())
