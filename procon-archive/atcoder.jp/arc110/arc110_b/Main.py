# import math
# # from decimal import *
# import numpy as np
#
# # from collections import deque, Counter
# import itertools
#
# # import sys
# import collections
# from collections import deque


if __name__ == '__main__':
    n = int(input())
    t = input()
    s = ""
    cnt = 0
    if t == "1":
        print(2*(10**10))
        exit()

    while len(s) < n + 10:
        s = s + "110"
        cnt += 1

    pans = 0
    for i in range(len(s)):
        if s[i:i+n] == t:
            pans += 1
    if pans > 0:
        print(10**10 - (cnt-pans))
    else:
        print(0)
















