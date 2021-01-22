# import math
# from decimal import *
# import numpy as np

# from collections import deque, Counter
# import itertools


# import sys
# import collections
from collections import deque


def ok(a, b, c, d):
    if a + b == c + d: return True
    if a - b == c - d: return True
    if abs(a - c) + abs(b - d) <= 3: return True


if __name__ == '__main__':
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    diff1 = r1 - c1
    diff2 = r2 - c2
    if r1 == r2 and c1 == c2:
        print(0)
        exit()
    if ok(r1, c1, r2, c2):
        print(1)
        exit()
    if (r1 - c1) % 2 == (r2 - c2) % 2:
        print(2)
        exit()
    for i in range(-4, 5):
        for j in range(-4, 5):
            if ok(r1, c1, r1 + i, c1 + j) and ok(r1 + i, c1 + j, r2, c2):
                print(2)
                exit()
    else:
        print(3)
        exit()
