import math
from decimal import *
import numpy as np
from collections import deque, Counter

if __name__ == '__main__':
    n = int(input())
    ans = 0
    for i in range(n):
        a, b = map(int, input().split())
        ans += int((a + b) * (b - a + 1) // 2)
    print(ans)
