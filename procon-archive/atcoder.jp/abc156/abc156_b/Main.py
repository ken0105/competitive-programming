import math
from decimal import *
import numpy as np

def div(syo, n,cnt):
    if syo == 0:
        print(cnt)
        exit()

    syo = syo // n
    cnt += 1
    div(syo,n,cnt)

if __name__ == '__main__':
    n,k = map(int,input().split())
    div(n,k,0)
