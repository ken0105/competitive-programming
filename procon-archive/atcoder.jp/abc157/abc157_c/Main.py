import math
from decimal import *
import numpy as np

if __name__ == '__main__':
    n, m = map(int, input().split())
    i_from = 0 + 10 ** (n - 1)
    if n == 1:
        i_from = 0
    i_to = 10 ** n - 1
    s_li = []
    c_li = []

    for i in range(m):
        s, c = map(int, input().split())
        s_li.append(s)
        c_li.append(c)

    for i in range(i_from, i_to + 1):
        str_i = str(i)
        bool_li = [True] * n
        for j in range(m):
            if str_i[s_li[j] - 1] != str(c_li[j]):
                bool_li[s_li[j] - 1] = False
        if False not in bool_li:
            print(i)
            exit()
    print(-1)
