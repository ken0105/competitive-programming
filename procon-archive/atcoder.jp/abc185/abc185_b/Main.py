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
import copy

if __name__ == '__main__':
    n,m,t = map(int,input().split())
    rest = 0
    b_a, b_b = 0, 0
    battery = n
    consume = 0
    for i in range(m):
        a,b = map(int,input().split())
        battery -= (a - b_b)
        if battery <= 0:
            print("No")
            exit()
        # if a - b_b >= n:
        #     print("No")
        #     exit()
        # consume += (a - b_b)
        battery = min(battery + (b-a), n)
        b_a, b_b = a,b
    #     if battery <= consume:
    #         print("No")
    #         exit()
    # print(consume)
    # print(battery)
    battery = battery - (t - b)
    if battery <= 0:
        print("No")
        exit()
    print("Yes")
