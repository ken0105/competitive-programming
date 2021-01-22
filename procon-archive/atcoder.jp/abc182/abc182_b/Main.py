import math
from decimal import *
import numpy as np
from collections import deque, Counter
import itertools

if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    max_gcd = [0] * 1500
    for i in range(2,max(a) + 1):
        for j in a:
            if j % i == 0:
                max_gcd[i] += 1
    for i in range(len(max_gcd)):
        if max_gcd[i] == max(max_gcd):
            print(i)
            exit()



