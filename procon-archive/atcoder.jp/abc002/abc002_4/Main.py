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
from itertools import combinations

if __name__ == '__main__':
    n, m = map(int, input().split())
    link = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(m):
        x, y = map(int, input().split())
        link[x][y] = 1
        link[y][x] = 1

    ans = 1
    for bit in range(2 ** n):
        group = []
        member = 0
        for i in range(n):
            if bit >> i & 1:
                group.append(i+1)
                member += 1
        if len(group) == 1:
            continue
        ok = True
        for c in combinations(group, 2):
            if link[c[0]][c[1]] != 1:
                ok = False
        if ok:
            ans = max(ans, member)
    print(ans)
