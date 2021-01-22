import math
from decimal import *
import numpy as np
from collections import deque, Counter



if __name__ == '__main__':
    n,k,m = map(int,input().split())
    a = list(map(int,input().split()))
    goal = m * n
    if goal - sum(a) > k:
        print(-1)
        exit()

    print(max(goal - sum(a),0))
