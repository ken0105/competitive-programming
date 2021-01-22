import math
from decimal import *
import numpy as np
from collections import deque
import collections

if __name__ == '__main__':
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    c = collections.Counter(s).most_common()
    cnt = c[0][1]

    l = []
    for i in c:
        if i[1] == cnt:
            l.append(i[0])
    l.sort()
    for i in l:
        print(i)


