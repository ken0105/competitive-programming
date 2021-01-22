import math
from decimal import *
import numpy as np


def is_cycle(word):
    w = word
    w_rev = ['_'] * (len(w))
    cnt = 0
    for k in range(len(w)-1, -1, -1):
        w_rev[cnt] = s[k]
        cnt += 1
    if w == w_rev:
        return True
    else:
        return False


if __name__ == '__main__':
    s = list(input())
    if is_cycle(s):
        if is_cycle(s[0:(len(s)-1)//2]):
            if is_cycle(s[(len(s)+3)//2 -1:]):
                print("Yes")
                exit()
    print("No")


