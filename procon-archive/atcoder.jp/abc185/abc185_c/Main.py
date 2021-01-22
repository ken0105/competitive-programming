# import math
# # from decimal import *
# import numpy as np
#
# # from collections import deque, Counter
# import itertools
#
# # import sys
# import collections
# from collections import deque
import copy
from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under


if __name__ == '__main__':
    l = int(input())
    n = l - 12
    m =12
    a = n +  m -1
    b = m -1
    print(cmb(a,b))

