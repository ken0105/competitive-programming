import math
from decimal import *
import numpy as np
from collections import deque, Counter
import itertools


if __name__ == '__main__':
    n = int(input())
    s, t = map(str,input().split())
    ans = ""
    for i in range(n):
        ans += s[i] + t[i]
    print(ans)


