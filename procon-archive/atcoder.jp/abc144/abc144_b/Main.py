import math
from decimal import *
import numpy as np
from collections import deque, Counter
import itertools

if __name__ == '__main__':
    kuku = []
    for i in range(1,10):
        for j in range(1,10):
            kuku.append(i*j)
    n = int(input())
    if n in kuku:
        print("Yes")
    else:
        print("No")

