import math
from decimal import *
import numpy as np
from collections import deque, Counter

if __name__ == '__main__':
    s = input()
    eightlist = []
    for i in range(100,1000):
        if i % 8 == 0:
            eightlist.append(str(i))
    if len(s) == 1:
        if s == "8":
            print("Yes")
            exit()
        else:
            print("No")
            exit()
    if len(s) == 2:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            print("Yes")
            exit()
        else:
            print("No")
            exit()
    s = list(s)
    s_temp = s.copy()
    if len(s) >= 3:
        for i in eightlist:
            s = s_temp.copy()
            if i[0] in s:
                s[s.index(i[0])] = 'x'
                if i[1] in s:
                    s[s.index(i[1])] = 'x'
                    if i[2] in s:
                        print("Yes")
                        exit()
    print("No")


