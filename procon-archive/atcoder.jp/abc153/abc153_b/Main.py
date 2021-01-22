import math
from decimal import *
import numpy as np
from collections import deque, Counter


if __name__ == '__main__':
    h,n = map(int,input().split())
    suma = sum(list(map(int,input().split())))
    if suma >= h:
        print("Yes")
    else:
        print("No")


