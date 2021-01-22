import math
from decimal import *
import numpy as np
from collections import deque, Counter
import itertools

if __name__ == '__main__':
   n = int(input())
   ans = 0
   for i in range(1,n+1):
       if i % 2 == 1:
           ans += 1
print(ans/n)
