import math
from decimal import *
import numpy as np
from collections import deque, Counter
import itertools

if __name__ == '__main__':
    a, b, x = map(int, input().split())

    def cost(n):
        return a * n + b * len(str(n))

    if cost(1) > x:
        print(0)
        exit()
    if cost(10 ** 9) <= x:
        print(10 ** 9)
        exit()
    start = 1
    end = 10 ** 9
    while end - start > 1:
        target = (start + end) // 2
        if x < cost(target):
            end = target
        else:
            start = target
    print(start)

