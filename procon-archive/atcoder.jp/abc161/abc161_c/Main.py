import math
from decimal import *
import numpy as np

if __name__ == '__main__':
    n,k = map(int,input().split())
    if n > k:
        p = n - ((n // k) * k)
        m = n - ((n // k + 1) * k)
        print(min(abs(p),abs(m)))
    if n <= k:
        print(min(n,abs(n-k)))

