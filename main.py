import random

from numpy import true_divide
def dice():
    number = [1 ,2 ,3 ,4 ,5 ,6 ]
    num_select = random.choices(number)
    print(num_select)
  
dice()