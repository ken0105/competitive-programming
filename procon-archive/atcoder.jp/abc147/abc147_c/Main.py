import math
from decimal import *
import numpy as np
from collections import deque, Counter
import itertools


if __name__ == '__main__':
    n =int(input())
    proofs = []
    for i in range(n):
        proofs.append([])
        a = int(input())
        for j in range(a):
            x,y = map(int,input().split())
            proofs[-1].append((x-1,y))


    def is_honest(i,j):
        return (i >> j) & 1

    def honest_count(i):
        cnt = 0
        for j in range(n):
            if i >> j & 1:
                cnt += 1
        return cnt

    ans = 0

    for i in range(1 << n):
        ok = True
        for j in range(n):
            if not is_honest(i,j):
                continue
            for x, y in proofs[j]:
                if y == 0 and is_honest(i,x):
                    ok = False
                if y == 1 and not is_honest(i,x):
                    ok = False
        if ok:
            ans = max(ans, honest_count(i))

    print(ans)



