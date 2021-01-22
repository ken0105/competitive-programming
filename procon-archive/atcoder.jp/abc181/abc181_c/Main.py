import math
from decimal import *
import numpy as np
from collections import deque, Counter

if __name__ == '__main__':
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int,input().split())))
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            for k in range(n):
                if i == k or j == k or i == j:
                    continue

                if (l[k][0] - l[j][0]) == 0:
                    a = float('inf')
                else:
                    a = (l[k][1] - l[j][1]) / (l[k][0] - l[j][0])


                if (l[j][0] - l[i][0]) == 0:
                    b = float('inf')
                else:
                    b = (l[j][1] - l[i][1]) / (l[j][0] - l[i][0])

                if a == b:
                    print("Yes")
                    exit()
    print("No")