import math
from decimal import *
import numpy as np

if __name__ == '__main__':
    n,m = map(int, input().split())
    a = list(map(int,input().split()))
    for i in a:
        n = n - i
    if n >= 0:
        print(n)
    else:
        print('-1')