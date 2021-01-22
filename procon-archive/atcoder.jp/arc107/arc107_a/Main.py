import math
from decimal import *
import numpy as np
from collections import deque, Counter

if __name__ == '__main__':
    a, b, c = map(int, input().split())
    a_sum = (1 + a) * a // 2
    b_sum = (1 + b) * b // 2
    c_sum = (1 + c) * c // 2
    ans = int((a_sum * b_sum * c_sum) % 998244353)
    print(ans)