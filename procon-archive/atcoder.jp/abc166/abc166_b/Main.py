import math
from decimal import *
import numpy as np

if __name__ == '__main__':
    n,k = map(int, input().split())
    l = [False] * n

    for i in range(k):
        skip = input()
        a = list(map(int, input().split()))
        for j in a:
            l[j -1] = True

    target = 0
    for i in l:
        if not i:
            target += 1
    print(target)

