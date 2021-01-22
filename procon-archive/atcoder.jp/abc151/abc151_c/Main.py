import math
from decimal import *
import numpy as np
from collections import deque, Counter

def getmap(d, n):
    try:
        return d[n]

    except:
        return 0

if __name__ == '__main__':
    n,m = map(int,input().split())
    d = dict()
    for i in range(m):
        p,s = map(str,input().split())
        if getmap(d,p+"AC") < 1:
           d[p + s] = getmap(d,p+s) + 1

    ac = 0
    wa = 0
    for i in range(1,n+1):
        if getmap(d,str(i)+"AC") == 1:
           ac += getmap(d,str(i)+"AC")
           wa += getmap(d,str(i)+"WA")
    print(ac,wa)

