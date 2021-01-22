# import math
# from decimal import *
# import numpy as np
# from collections import deque, Counter
# import itertools
import sys

if __name__ == '__main__':
    s = input()
    t = input()
    ans = 0
    for i in range(len(s)):
        if s[i] == t[i]:
            ans += 1
    print(ans)







