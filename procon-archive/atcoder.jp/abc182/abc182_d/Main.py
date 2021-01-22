# import math
# from decimal import *
# import numpy as np
# from collections import deque, Counter
# import itertools

if __name__ == '__main__':
    n = int(input())
    a = [0] + list(map(int, input().split()))
    n += 1

    accum_sum = a[:]
    for i in range(1,n):
        accum_sum[i] += accum_sum[i-1]
    accum_max = accum_sum[:]
    accum_accum = accum_sum[:]
    for i in range(1,n):
        accum_max[i] = max(accum_max[i-1],accum_max[i])
        accum_accum[i] = accum_accum[i-1] + accum_accum[i]
    ans = 0
    now = 0
    for i in range(1,n):
        if i != n-1:
            ans = max(ans, accum_accum[i] + accum_max[i])
        else:
            ans = max(ans, accum_accum[i])
        accum_accum[i] += accum_sum[i]
    print(ans)





