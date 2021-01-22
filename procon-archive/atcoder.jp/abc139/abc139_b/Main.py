import math
# from decimal import *
# import numpy as np
# from collections import deque, Counter
# import itertools
import sys

if __name__ == '__main__':
    a,b = map(int,input().split())
    yet, ans = a, 1
    if b == 1:
        print(0)
        exit()
        
    while yet < b:
        yet += a - 1
        ans += 1
    print(ans)








