import math
from decimal import *
import numpy as np
from collections import deque, Counter
import itertools

if __name__ == '__main__':
    n = input()
    mindelnum = 20
    for bit in range(2 ** len(n)):
        num = ""
        delnum = 0
        for i in range(len(n)):
            if (bit >> i) % 2 == 1:
                num += n[i]
            else:
                delnum += 1
        if num != "" and int(num) % 3 == 0:
            mindelnum = min(mindelnum, delnum)
    if mindelnum == 20:
        print(-1)
        exit()
    else:
        print(mindelnum)






