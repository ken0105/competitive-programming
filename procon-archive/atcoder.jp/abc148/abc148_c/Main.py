import math
from decimal import *
import numpy as np
from collections import deque, Counter
import itertools


if __name__ == '__main__':
    a,b = map(int,input().split())
    ans = a * b // math.gcd(a,b)
    print(ans)


