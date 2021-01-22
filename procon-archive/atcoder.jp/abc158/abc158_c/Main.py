import math
from decimal import *
import numpy as np

if __name__ == '__main__':
    a, b = map(int, input().split())
    for i in range(1, 15000):
        tax8 = math.floor(i * 8 / 100)
        tax10 = math.floor(i * 10 / 100)
        if tax8 == a and tax10 == b:
            print(i)
            exit()
    print(-1)
