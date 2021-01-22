import math
from decimal import *
import numpy as np
from collections import deque, Counter
import itertools

if __name__ == '__main__':
   n,k = map(int,input().split())
   h = list(map(int,input().split()))
   ans = 0
   for i in range(n):
       if h[i] >= k:
           ans += 1
print(ans)