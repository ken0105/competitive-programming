# import math
# from decimal import *
import numpy as np

# from collections import deque, Counter
# import itertools
# import sys
# import collections

if __name__ == '__main__':
    n = int(input())
    ans = 0
    for i in range(1,n+1):
        cnt = 0
        for j in range(1,i+1):
            if i % j == 0:
                cnt += 1
        if cnt == 8 and i % 2 == 1:
            ans += 1
    print(ans)
