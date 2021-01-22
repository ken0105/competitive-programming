import math
# from decimal import *
# import numpy as np
# from collections import deque, Counter
# import itertools
import sys


def lcm(x, y):
    return x * y // math.gcd(x, y)


if __name__ == '__main__':
    n = input()
    a = list(map(int,input().split()))

    child = 0
    tmp_lcm = a[0]
    for i in a:
        tmp_lcm = lcm(i, tmp_lcm)
    for i in a:
        child += tmp_lcm // i
    print(tmp_lcm/child)








