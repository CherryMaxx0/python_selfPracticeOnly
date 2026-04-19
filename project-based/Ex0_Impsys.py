# from ..initial_learning.Le9 import Dice
#this is wrong

import sys
# sys.path.insert(0,"../")
# from initial_learning.Le9 import Dice


# sys.path.append(r"c:\CMX\CMX everything PC\EVERY - Projects CMX-PC\Coding\Python_learning\initial_learning")
# from Le9 import Dice

sys.path.append("..")
from initial_learning.Le9 import Dice



dicee = Dice()
print(dicee.roll())


