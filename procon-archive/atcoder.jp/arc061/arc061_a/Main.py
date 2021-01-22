import math
from decimal import *
import numpy as np

if __name__ == '__main__':
    s = input()
    s_len = len(s)
    sum_num = 0

    for i in range( 2 ** (s_len - 1) ):
        f = s[0]
        for j in range(s_len - 1):
            if i >> j & 1:
                f = f + s[j + 1]
            else:
                f = f + '+' + s[j + 1]
        sum_num += sum(map(int, f.split("+")))
    print(sum_num)