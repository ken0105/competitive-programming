# import math
# # from decimal import *
# import numpy as np
#
# # from collections import deque, Counter
# import itertools
#
# # import sys
# import collections
# from collections import deque
# import copy

if __name__ == '__main__':
    h,w = map(int,input().split())
    a = []
    for i in range(h):
        a.append(list(map(int,input().split())))

    min_value = 200
    for i in range(h):
        for j in range(w):
            if a[i][j] < min_value:
                min_value = a[i][j]

    ans = 0

    for i in range(h):
        for j in range(w):
            ans += a[i][j] - min_value

    print(ans)


