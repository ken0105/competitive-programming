import math
from decimal import *
import numpy as np
from collections import deque, Counter

if __name__ == '__main__':
    n = int(input())
    s = input()
    ans = 0
    for i in range(len(s)):
        if s[i:i+3] == "ABC":
            ans += 1
    print(ans)

