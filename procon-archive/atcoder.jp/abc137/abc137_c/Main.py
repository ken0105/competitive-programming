import math
# from decimal import *
# import numpy as np
# from collections import deque, Counter
# import itertools
import sys
import collections

if __name__ == '__main__':
    n = int(input())
    word_list = []
    for i in range(n):
        s = list(input())
        s.sort()
        s = str(s)
        word_list.append(s)
    c = collections.Counter(word_list)
    values = list(c.values())
    ans = 0
    for value in values:
        ans += value * (value -1 ) // 2

    print(ans)










