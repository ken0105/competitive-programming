# import math
# from decimal import *
import numpy as np

# from collections import deque, Counter
import itertools

# import sys
# import collections

if __name__ == '__main__':
    a, b, c, x, y = map(int, input().split())
    efficient = "single"
    if c * 2 < a + b:
        efficient = "half"
    money = 0
    if efficient == "half":
        money += c * 2 * min(x, y)
        half_amount = min(x,y)
        rest_x = x - half_amount
        rest_y = y - half_amount
        money += a * rest_x + b * rest_y
        money = min(money, c*2*max(x,y))
    else:
        money = a * x + b*y
    print(money)
