import math
from decimal import *
import numpy as np
from collections import deque, Counter
import itertools

if __name__ == '__main__':
    s = input()
    odd = ['R', 'U', 'D']
    even = ['L', 'U', 'D']
    for i in range(len(s)):
        if (i + 1) % 2 == 1:
            if s[i] not in odd:
                print("No")
                exit()
        else:
            if s[i] not in even:
                print("No")
                exit()
    print("Yes")
