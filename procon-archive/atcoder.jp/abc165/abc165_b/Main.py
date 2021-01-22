import math
from decimal import *
import numpy as np

if __name__ == '__main__':
    x = int(input())
    year = 0
    s = 100

    while True:
        year += 1
        s += int(s // 100)
        if s >= x:
            print(year)
            exit()
