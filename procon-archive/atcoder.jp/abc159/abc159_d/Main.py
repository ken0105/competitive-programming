from itertools import product
from collections import Counter
from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under


if __name__ == '__main__':
    N = int(input())
    A = list(map(int,input().split()))
    c = Counter(A)
    ans = 0
    for k in c:
        value = c[k]
        if value >= 2:
            ans += cmb(value,2)

    for a in A:
        value = c[a]
        before = 0
        after = 0
        if value >= 2:
            before = cmb(value,2)
        if value - 1 >=2:
            after = cmb(value-1,2)
        diff = before - after
        print(ans - diff)

