# import math
# # from decimal import *
# import numpy as np
#
# # from collections import deque, Counter
import itertools
#
# # import sys
# import collections
# from collections import deque
# import copy
from typing import List
import random


if __name__ == '__main__':
    n = int(input())
    p = []
    l = []
    for _ in range(n):
        x,y = map(int,input().split())
        p.append(x)
        p.append(y)
        l.append((x,y))
    ans = float('inf')

    for i in itertools.permutations(p, 2):
        dist = 0
        for j in l:
            dist += abs(i[1] - j[1]) + abs(j[1] - j[0]) + abs(j[0] - i[0])
        ans = min(ans, dist)
    print(ans)

