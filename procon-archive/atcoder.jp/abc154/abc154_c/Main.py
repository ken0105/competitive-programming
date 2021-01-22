import math
from decimal import *
import numpy as np
from collections import deque

if __name__ == '__main__':
    n = int(input())
    s = set(map(int,input().split()))
    if n == len(s):
        print("YES")
    else:
        print("NO")


