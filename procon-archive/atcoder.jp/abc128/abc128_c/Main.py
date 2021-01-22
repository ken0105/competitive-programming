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
    n,m = map(int,input().split())
    k = []
    s = []
    for _ in range(m):
        tmp = list(map(int, input().split()))
        k.append(tmp[0])
        s.append(tmp[1:])
    p = list(map(int,input().split()))
    ans = 0
    for bit in range(2**n):
        s_status = []
        for i in range(n):
            if bit >> i & 1:
                s_status.append(True)
            else:
                s_status.append(False)
        ok = True
        for i in range(len(k)):
            on_cnt = 0
            for j in s[i]:
                if s_status[j - 1]:
                    on_cnt += 1
            if on_cnt % 2 != p[i]:
                ok = False
        if ok:
            ans += 1
    print(ans)