import math
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
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int,input().split())))

    dist = 0
    cnt = 0
    for i in itertools.permutations(l,n):
        cnt += 1
        for j in range(n-1):
            dist += math.sqrt((i[j][0] - i[j+1][0]) ** 2 + (i[j][1] - i[j+1][1]) ** 2)
    print('{:.10f}'.format(dist/cnt))