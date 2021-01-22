import math
from decimal import *
import numpy as np
from collections import deque, Counter
import itertools

if __name__ == '__main__':
    a,b = map(int,input().split())
    if a <= 9 and b <= 9:
        print(a*b)
    else:
        print(-1)


