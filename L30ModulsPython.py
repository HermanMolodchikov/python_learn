# https://docs.python.org/3/library/

# import os
# import random as r
# import random
# from random import randint, shuffle
# from random import *

# import os
# import os as my
#
# print(os.getcwd())
# print(my.getcwd())

# print(os.getcwd())
# print(random.randint(1, 100))
# print(randint(1, 100))

# l1 = [1, 2, 3, 4, 5]
# shuffle(l1)
# print(l1)


import libs
from libs import get_count, get_len

f = libs.get_count
print(__name__)
print(libs.get_count('hello', 'l'))
print(libs.get_len('hello'))
print(get_count('hello', 'l'))
print(get_len('hello'))
print(f('Hello', 'l'))


def get_sum(a, b):
    return a + b

func = get_sum
print(func(5, 2))