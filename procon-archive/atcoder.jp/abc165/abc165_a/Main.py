import math
from decimal import *
import numpy as np

if __name__ == '__main__':
    k = int(input())
    a, b = map(int, input().split())

    if a % k == 0 or b %k == 0:
        print("OK")
        exit()

    if a // k == b // k:
        print("NG")
    else:
        print("OK")
