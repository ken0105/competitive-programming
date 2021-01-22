import math
# from decimal import *
# import numpy as np
# from collections import deque, Counter
import itertools
import sys
import collections

if __name__ == '__main__':
    n,k = map(int,input().split())
    t = []
    for i in range(n):
        a = list(map(int,input().split()))
        t.append(a)
    l = [ i for i in range(1,n)]
    ans = 0
    for v in itertools.permutations(l,n-1):
        now = 0
        dist = 0
        for j in range(len(v)):
            dist += t[now][v[j]]
            now = v[j]
        dist += t[now][0]
        if dist == k:
            ans += 1
    print(ans)
