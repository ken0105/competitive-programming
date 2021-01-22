import math
from decimal import *
import numpy as np

if __name__ == '__main__':
    cnt = 0
    k = int(input())
    for i in range(1,k+1):
        for j in range(1,k+1):
            gcd_tmp = math.gcd(i,j)
            for l in range(1,k+1):
                cnt += math.gcd(gcd_tmp, l)
    print(cnt)

