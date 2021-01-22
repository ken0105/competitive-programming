# import math
# from decimal import *
import numpy as np
# from collections import deque, Counter
# import itertools
# import sys
# import collections

if __name__ == '__main__':
    n,w = map(int,input().split())
    demand = [0] * 220000
    for _ in range(n):
        s,t,p = map(int,input().split())
        demand[s] += p
        demand[t] -= p

    for i in range(1,220000):
        demand[i] += demand[i-1]

    if max(demand) > w:
        print("No")
    else:
        print("Yes")
