import math
# from decimal import *
# import numpy as np
# from collections import deque, Counter
# import itertools
import sys

if __name__ == '__main__':
    k,x = map(int, input().split())
    start = x - k +1
    end = x + k -1
    ans = ""
    for i in range(start, end+1):
        ans += str(i) + " "
    print(ans)









