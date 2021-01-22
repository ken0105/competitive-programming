import math
from decimal import *
import numpy as np
from collections import deque, Counter
import itertools

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    d = {a[key]: key + 1 for key in range(n)}
    ans = ""
    for i in range(1,n + 1):
        ans += str(d[i]) + " "
    print(ans)
