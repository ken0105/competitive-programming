import math
# # from decimal import *
# import numpy as np
#
# # from collections import deque, Counter
# import itertools
#
# # import sys
# import collections
# from collections import deque
import copy

if __name__ == '__main__':
    n,m = map(int,input().split())
    a = list(map(int,input().split())) + [0, n + 1]
    segment = []
    a.sort()
    for i in range(1,len(a)):
        segment.append(a[i] - a[i-1] - 1)
    segment.sort(reverse=True)
    while len(segment) > 0 and segment[-1] == 0:
        segment.pop()
    if len(segment) == 0:
        print(0)
        exit()

    k = segment[-1]
    ans = 0
    for i in segment:
        ans += math.ceil(i/k)
    print(ans)


