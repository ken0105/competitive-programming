# import math
# from decimal import *
import numpy as np

# from collections import deque, Counter
import itertools

# import sys
import collections
from collections import deque

if __name__ == '__main__':
    a, b, x, y = map(int, input().split())
    up = True
    if a > b:
        up = False
    ans = 0
    if a == b:
        print(x)
        exit()
    if up:
        ans = 3 * x + 2 * x * (b - a - 1)
        ans = min(ans, x + (b - a) * y)
    if not up:
        ans = x + 2 * x * (a - b- 1)
        ans = min(ans, y + x + (a - b - 1) * y)
        ans = min(ans, x + (a-b-1)*y)
    print(ans)