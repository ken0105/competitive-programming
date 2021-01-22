import math
from decimal import *
import numpy as np
from collections import deque, Counter


def f(s, n):
    mina = max(1, s - n)
    maxa = min(n, s - 1)
    return max(maxa - mina + 1,0)


if __name__ == '__main__':
    cnt = 0
    n, k = map(int, input().split())
    for i in range(2, 2 * n + 1):
        cnt += f(i,n) * f(i-k,n)
    print(cnt)