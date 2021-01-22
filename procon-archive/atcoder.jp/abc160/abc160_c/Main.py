import math
from decimal import *
import numpy as np

if __name__ == '__main__':
    k, n, = map(int, input().split())
    a = list(map(int, input().split()))

    max_dist = 0
    for i in range(n):
        if i == 0:
            max_dist = k + a[0] - a[-1]
            continue
        max_dist = max(max_dist, a[i] - a[i - 1])
    print(k - max_dist)
