import math
from decimal import *
import numpy as np
from collections import deque, Counter


if __name__ == '__main__':
    h,a = map(int,input().split())
    ans = math.ceil(h/a)
    print(ans)


