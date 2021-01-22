import math
from decimal import *
import numpy as np
from collections import deque, Counter
import itertools


if __name__ == '__main__':
    s = input()
    rs = s[::-1][:]
    cnt = 0
    for i in range(len(s)):
        if s[i] != rs[i]:
            cnt += 1
    print(cnt // 2)


