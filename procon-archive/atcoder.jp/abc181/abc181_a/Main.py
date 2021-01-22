import math
from decimal import *
import numpy as np
from collections import deque, Counter

if __name__ == '__main__':
    n = int(input())
    if n % 2 == 0:
        print("White")
    else:
        print("Black")