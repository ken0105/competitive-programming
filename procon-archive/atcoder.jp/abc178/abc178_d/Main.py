import math
from functools import reduce
from operator import mul


def cmb(n, r):
    r = min(n - r, r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


if __name__ == '__main__':
    s = int(input())
    div_max = s // 3 - 1
    ans = 0
    for i in range(div_max + 1):
        ans += cmb(s-(3*(i+1))+i, s-(3*(i+1)))
    print(ans % (10 ** 9 + 7))
