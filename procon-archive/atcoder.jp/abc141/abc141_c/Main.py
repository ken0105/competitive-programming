import math
from decimal import *
import numpy as np
from collections import deque, Counter
import itertools

if __name__ == '__main__':
    n,k,q = map(int,input().split())
    a = []
    for i in range(q):
        a.append(int(input()))
    member = [0] * n
    min_ans = q - k
    for i in a:
        member[i-1] += 1

    for i in member:
        if i - min_ans >0:
            print('Yes')
        else:
            print('No')

