import math
# from decimal import *
# import numpy as np
# from collections import deque, Counter
# import itertools
import sys
import collections

if __name__ == '__main__':
    sx, sy, gx, gy = map(int,input().split())
    a =  (sy+gy)/(gx-sx)
    print(sy/a + sx)