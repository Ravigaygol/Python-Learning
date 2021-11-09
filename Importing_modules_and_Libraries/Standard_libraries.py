#Standard library comes with python 
#useful methods

# 1- Random = giving random value

import random

types_of_drinks = ['soda', 'coffee', 'water', 'tea']
print(random.choice(types_of_drinks))

print('*' * 98)
#***********************************************************************
# 2- randomint = giving random integer value within mention length

print(random.randint(1,10))

print('*' * 98)
import math

square_root = math.sqrt(64)
print(square_root)

#************************************************************************
# 3- Time
print('*' * 98)
import time
print(time.asctime())
print(time.timezone)

print('*' * 98)
#***********************************************************************

import sys
for path in sys.path:
    print(path)
    