import math
from decimal import *
import numpy as np

if __name__ == '__main__':
    n,r = map(int,input().split())
    if n >= 10:
        print(r)
        exit()
    else:
        print(r + 100 * (10 -n))
