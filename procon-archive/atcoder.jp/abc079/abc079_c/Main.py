import math
from decimal import *
import numpy as np
from collections import deque, Counter

if __name__ == '__main__':
    s = input()
    ope = len(s) - 1
    for i in range(ope ** 2):
        ans = int(s[0])
        ans_str = s[0]
        for j in range(ope):
            if (i >> j) & 1:
                ans += int(s[j+1])
                ans_str += "+" + s[j+1]
            else:
                ans -= int(s[j+1])
                ans_str += "-" + s[j+1]
        if ans == 7:
            print(ans_str + "=7")
            exit()



