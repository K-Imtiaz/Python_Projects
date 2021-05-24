#This code is all about Random module

import random
import My_module

random_integer=random.randint(1, 200)
print(random_integer)
print(My_module.S)
print(My_module.F)
print(My_module.pi)

#random_integer=random.randint(1, 200)
#print(random_integer)
print(My_module.S)
print(My_module.F)
print(My_module.pi)

random_float=random.random()*5
print(random_float)

Love_score=random.randint(1, 100)
print(f"Your love score is {Love_score}%")