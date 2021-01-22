# import math
# from decimal import *
import numpy as np

# from collections import deque, Counter
# import itertools
# import sys
# import collections

if __name__ == '__main__':
    acgt = ["A", "C", "G", "T"]
    s = input()
    ans = 0
    now = 0
    for i in range(len(s)):
        if s[i] in acgt:
            now += 1
        else:
            now = 0
        ans = max(now,ans)
    print(ans)
