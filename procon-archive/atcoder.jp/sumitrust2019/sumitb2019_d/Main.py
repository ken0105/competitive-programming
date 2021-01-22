# import math
# from decimal import *
import numpy as np

# from collections import deque, Counter
import itertools

# import sys
# import collections

if __name__ == '__main__':
    n = int(input())
    s = input()
    ans = 0
    luckies = []
    for i in range(10):
        for j in range(10):
            for k in range(10):
                luckies.append(str(str(i) + str(j) + str(k)))
    for lucky in luckies:
        try:
            if lucky[0] in s:
                index1 = s.find(lucky[0])
                if lucky[1] in s[index1+1:]:
                    index2 = s.find(lucky[1],index1+1)
                    if lucky[2] in s[index2+1:]:
                        ans += 1
        except:
            continue
    print(ans)
