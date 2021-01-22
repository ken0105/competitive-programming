# import math
# from decimal import *
# import numpy as np
# from collections import deque, Counter
# import itertools

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(len(a)):
        a[i] = a[i] - 1

    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ans = 0
    before = -100
    for i in range(0,len(a)):
        ans += b[a[i]]
        if before + 1 == a[i]:
            ans += c[before]
        before = a[i]
    print(ans)








