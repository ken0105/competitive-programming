import math
from decimal import *
import numpy as np

if __name__ == '__main__':
    a = []
    for i in range(3):
        a.append(list(map(int, input().split())))
    n = int(input())
    for i in range(n):
        b = int(input())
        for j in range(len(a)):
            for k in range(3):
                if a[j][k] == b:
                    a[j][k] = -1
    if a[0] == [-1,-1,-1] or a[1] == [-1,-1,-1] or a[2] == [-1,-1,-1] or (a[0][0] == -1 and a[1][1] == -1 and a[2][2] == -1) or (a[0][2] == -1 and a[1][1] == -1 and a[2][0] == -1)\
            or (a[0][0] == -1 and a[1][0] == -1 and a[2][0] == -1) or (a[0][1] == -1 and a[1][1] == -1 and a[2][1] == -1) or (a[0][2] == -1 and a[1][2] == -1 and a[2][2] == -1):
        print("Yes")
    else:
        print("No")
