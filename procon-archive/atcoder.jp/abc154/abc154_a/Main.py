import math
from decimal import *
import numpy as np
from collections import deque

if __name__ == '__main__':
    s,t = map(str,input().split())
    a,b = map(int,input().split())
    u = input()
    if s == u:
        print(a-1, b)
    else:
        print(a, b-1)


