import random


class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second


#this is to prevent twice execution when imported to other file. It will only be excute if run from this python file

if __name__ == '__main__': 
    dice = Dice()
    print(dice.roll())
