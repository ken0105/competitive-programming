import math
from decimal import *
import numpy as np

if __name__ == '__main__':
    x = int(input())
    five = x // 500
    rest = x - 500 * five
    fiveh = rest // 5
    print(five * 1000 + fiveh * 5)
