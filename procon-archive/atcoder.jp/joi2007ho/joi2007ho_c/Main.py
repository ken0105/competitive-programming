# import math
# from decimal import *
import numpy as np

# from collections import deque, Counter
import itertools


# import sys
# import collections


if __name__ == '__main__':
    n = int(input())
    l = [tuple(map(int, input().split())) for _ in range(n)]
    set_l = set(l)
    # print(set_l)
    ans = 0
    for i in itertools.combinations(set_l, 2):
        vectorx = abs(i[1][0] - i [0][0])
        vectory = abs(i[1][1] - i [0][1])
        # print(i,vectorx,vectory)
        if (i[1][0] - vectory, i[1][1] - vectorx) in set_l and (i[0][0] - vectory, i[0][1] - vectorx) in set_l:
            # print((i[1][0] - vectory, i[1][1] - vectorx))
            # print((i[0][0] - vectory, i[0][1] - vectorx))
            # print(i)
            ans = max(ans, vectorx **2 + vectory **2)
    print(ans)