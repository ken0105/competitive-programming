import math
from decimal import *
import numpy as np
from collections import deque, Counter



if __name__ == '__main__':
    n = int(input())
    l = list(map(int,input().split()))
    cnt = 0
    minnum = l[0]
    for i in l:
        if minnum >= i:
            cnt +=1
            minnum = i
    print(cnt)