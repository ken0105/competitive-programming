# import math
# from decimal import *
# import numpy as np

# from collections import deque, Counter
# import itertools


# import sys
# import collections
from collections import deque


if __name__ == '__main__':
    n = int(input())
    s = input()
    d = deque([])
    for i in range(n):
        d.append(s[i])
        if len(d) < 3:
            continue
        if d[-3] + d[-2] + d[-1] == "fox":
            for i in range(3):
                d.pop()
    print(len(d))