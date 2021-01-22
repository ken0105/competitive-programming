import math
from decimal import *
import numpy as np
from collections import deque, Counter

if __name__ == '__main__':
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort()
    try:
        for i in range(k):
            h.pop()
    except:
        pass
    print(sum(h))
