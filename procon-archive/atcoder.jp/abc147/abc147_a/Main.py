import math
from decimal import *
import numpy as np
from collections import deque, Counter
import itertools


if __name__ == '__main__':
    a = list(map(int,input().split()))
    if sum(a) >= 22:
        print("bust")
    else:
        print("win")


