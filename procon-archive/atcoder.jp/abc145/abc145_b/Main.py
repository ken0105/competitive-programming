import math
from decimal import *
import numpy as np
from collections import deque, Counter
import itertools

if __name__ == '__main__':
    n = int(input())
    s = input()
    mid = math.ceil(n/2)
    if s[0:mid] == s[mid:]:
        print("Yes")
    else:
        print("No")

