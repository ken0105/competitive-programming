import math
from decimal import *
import numpy as np

if __name__ == '__main__':
    n = int(input())
    s = set()
    for i in range(n):
        s.add(input())
    print(len(s))