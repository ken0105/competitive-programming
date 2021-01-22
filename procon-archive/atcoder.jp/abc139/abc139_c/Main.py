import math
# from decimal import *
# import numpy as np
# from collections import deque, Counter
# import itertools
import sys

if __name__ == '__main__':
    n = int(input())
    h = list(map(int,input().split()))
    now = 0
    ans = 0
    for i in range(len(h)):
        if i != len(h) - 1:
            if h[i + 1] <= h[i]:
                now += 1
                ans = max(ans, now)
            else:
                now = 0
    print(ans)








