# import math
# from decimal import *
# import numpy as np
# from collections import deque, Counter
# import itertools
import sys

if __name__ == '__main__':
    n = int(input())
    b = list(map(int,input().split()))
    a = []
    for i in range(n):
        if i == 0:
            a.append(b[i])
        elif i == n -1:
            a.append(b[i-1])
        else:
            a.append(min(b[i-1],b[i]))
    print(sum(a))








