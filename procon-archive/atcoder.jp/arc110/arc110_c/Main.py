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
import copy

if __name__ == '__main__':
    n = int(input())
    p = list(map(lambda x: int(x) - 1, input().split()))
    used = [False] * n
    ans = []
    for i in range(n):
        while i > 0 and p[i - 1] > p[i]:
            if used[i]:
                print(-1)
                exit()
            used[i] = True
            ans.append(i)
            p[i], p[i - 1] = p[i - 1], p[i]
            i -= 1
    if len(ans) == n - 1:
        print(*ans, sep='\n')
    else:
        print(-1)
