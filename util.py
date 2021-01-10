import math
from operator import mul
from functools import reduce


class Utils:
    # 素数判定
    def is_prime(self, num):
        for i in range(2,num):
            if i ** 2 > num:
                break
            if num % i == 0:
                return False
        return True

    # 最小公倍数
    def lcm(self, x, y):
        return x * y // math.gcd(x, y)

    # 組み合わせの数
    def cmb(self, n, r):
        r = min(n - r, r)
        if r == 0: return 1
        over = reduce(mul, range(n, n - r, -1))
        under = reduce(mul, range(1, r + 1))
        return over // under