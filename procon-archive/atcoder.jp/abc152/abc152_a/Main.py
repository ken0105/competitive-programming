import math
from decimal import *
import numpy as np
from collections import deque, Counter



if __name__ == '__main__':
    n,m = map(int,input().split())
    if n == m:
        print("Yes")
    else:
        print("No")