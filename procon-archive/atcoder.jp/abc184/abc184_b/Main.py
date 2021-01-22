# import math
# from decimal import *
# import numpy as np

# from collections import deque, Counter
# import itertools


# import sys
# import collections
from collections import deque

if __name__ == '__main__':
    n,x =  map(int,input().split())
    s = input()
    for i in range(n):
        if s[i] == "x" and x > 0:
            x -= 1
        if s[i] == "o":
            x += 1
    print(x)