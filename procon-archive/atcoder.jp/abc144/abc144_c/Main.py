import math
from decimal import *
import numpy as np
from collections import deque, Counter
import itertools

if __name__ == '__main__':
    n = int(input())
    ans = 10 ** 12
    for i in range(1,math.floor(math.sqrt(n)) + 1):
        if n % i != 0:
            continue
        else:
            ans = min(ans,(n//i + i))
    print(ans-2)