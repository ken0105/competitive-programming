import math
from decimal import *
import numpy as np
from collections import deque, Counter
import itertools

if __name__ == '__main__':
    a,b,k = map(int,input().split())
    if a <= k:
        k = k - a
        a = 0
        b = max(b - k,0)
    else:
        a = a - k
        k = 0
    print(a,b)

