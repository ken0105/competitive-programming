import math
# from decimal import *
import numpy as np

# from collections import deque, Counter
import itertools

# import sys
import collections
from collections import deque


# 最小公倍数
def lcm(x, y):
    return x * y // math.gcd(x, y)


if __name__ == '__main__':
    n = int(input())
    l = []
    for i in range(2,n+1):
        l.append(i)
    ans = 1

    for i in range(len(l)):
        ans = lcm(ans,l[i])
    print(ans + 1)
















