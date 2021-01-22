# import math
# from decimal import *
# import numpy as np

# from collections import deque, Counter
# import itertools


# import sys
# import collections
from collections import deque

if __name__ == '__main__':
    s, p = map(int, input().split())
    for i in range(1,p+1):
        if i * i > p:
            break
        if p % i == 0:
            if p // i + i == s:
                print("Yes")
                exit()
    print("No")
    exit()