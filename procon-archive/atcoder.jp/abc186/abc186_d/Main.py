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
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()

    a_sum = [a[0]]

    for i in range(1,n):
        a_sum.append(a_sum[i-1] + a[i])

    ans = 0
    for i in range(n):
        follow = n - i - 1
        ans += abs(a[i] * follow - (a_sum[-1] - a_sum[i]))
    print(ans)



