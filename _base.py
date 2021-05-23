from functools import reduce
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
from operator import mul
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7

def main():



def is_prime(num):
    for i in range(2,num):
        if i ** 2 > num:
            break
        if num % i == 0:
            return False
    return True

def lcm(x, y):
    return x * y // math.gcd(x, y)


def cmb(n, r):
    r = min(n - r, r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


if __name__ == '__main__':
    main()
