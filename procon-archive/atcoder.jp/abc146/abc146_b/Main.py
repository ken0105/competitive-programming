import math
from decimal import *
import numpy as np
from collections import deque, Counter
import itertools

if __name__ == '__main__':
    n = int(input())
    s = list(input())
    for i in range(len(s)):
        if ord(s[i]) + n > ord("Z"):
            s[i] = chr(ord(s[i]) + n - 26)
        else:
            s[i] = chr(ord(s[i]) + n)
    ans = ""
    for i in s:
        ans += i
    print(ans)
