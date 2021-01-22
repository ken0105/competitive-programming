import math
from decimal import *
import numpy as np
from collections import deque, Counter

if __name__ == '__main__':
    k, x = map(int,input().split())
    if k * 500 >= x: print("Yes")
    else: print("No")


