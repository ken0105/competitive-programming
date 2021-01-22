import math
from decimal import *
import numpy as np

if __name__ == '__main__':
    n = int(input())
    li = list(map(int,input().split()))
    x_sum = sum(li)
    ave = round(x_sum / n)

    ans = 0
    for i in li:
        ans += (i - ave) ** 2
    print(ans)

