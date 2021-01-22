import math
from decimal import *
import numpy as np

if __name__ == '__main__':
    s,w = map(int,input().split())
    if w >= s:
        print("unsafe")
    else:
        print("safe")