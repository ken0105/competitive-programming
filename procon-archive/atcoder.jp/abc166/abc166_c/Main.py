import math
from decimal import *
import numpy as np

if __name__ == '__main__':
    n,m = map(int,input().split())
    h = list(map(int,input().split()))
    good = [True] * n
    for i in range(m):
        a,b = map(int,input().split())
        a_height = h[a-1]
        b_height = h[b-1]
        if a_height > b_height:
            good[b-1] = False
        elif a_height < b_height:
            good[a-1] = False
        else:
            good[b-1] = False
            good[a-1] = False
    cnt = 0
    for i in good:
        if i:
            cnt += 1
    print(cnt)



