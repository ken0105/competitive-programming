import math
from decimal import *
import numpy as np

if __name__ == '__main__':
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    fav = 0

    a_sum = sum(a)
    for i in a:
        if i >= (1/(4*m))*a_sum:
            fav += 1

    if fav >= m:
        print('Yes')
    else:
        print('No')

