import math
from decimal import *
import numpy as np

if __name__ == '__main__':
    n, m = map(int, input().split())
    com = (n + m) * (n + m - 1) /2
    print(int(com - n *m))