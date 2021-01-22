import math
from decimal import *
import numpy as np


if __name__ == '__main__':
    n,a,b = map(int,input().split())
    cnt = n // (a+b)
    amari = n - (a+b) * cnt
    if amari <= a:
        print(amari + a*cnt)
    else:
        print(a + a*cnt)



