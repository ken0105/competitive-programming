import math
# from decimal import *
# import numpy as np
# from collections import deque, Counter
# import itertools
import sys


def merge(x,y):
    return (x + y) / 2


if __name__ == '__main__':
    n = input()
    v = list(map(int,input().split()))
    v2 = []
    v.sort()
    while len(v) > 1:
        v.append(merge(v[0], v[1]))
        v.remove(v[0])
        v.remove(v[0])
        v.sort()

    print(v[0])









