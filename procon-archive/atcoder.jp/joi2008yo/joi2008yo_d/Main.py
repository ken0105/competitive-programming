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
    m = int(input())
    sm = []
    sn = []
    for _ in range(m):
        (x,y) = map(int, input().split())
        sm.append((x,y))
    n = int(input())
    for _ in range(n):
        (x,y) = map(int, input().split())
        sn.append((x,y))
    sn = set(sn)
    base = sm[0]
    for i in sn:
        vector_x = i[0] - base[0]
        vector_y = i[1] - base[1]
        ok = True
        for j in sm:
            if (j[0] + vector_x, j[1] + vector_y) not in sn:
                ok = False
        if ok:
            print(vector_x, vector_y)
            exit()

