import math
from decimal import *
import numpy as np
from collections import deque, Counter



if __name__ == '__main__':
    a,b = map(int,input().split())
    alist,blist ="", ""
    for i in range(b):
        alist += str(a)
    for i in range(a):
        blist += str(b)
    li = [alist,blist]
    li.sort()
    print(li[0])