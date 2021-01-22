import math
from decimal import *
import numpy as np

if __name__ == '__main__':
    n = int(input())
    li = list(map(int,input().split()))
    subordinate = [0] * n

    for i in li:
        subordinate[i-1] += 1

    for i in subordinate:
        print(i)
