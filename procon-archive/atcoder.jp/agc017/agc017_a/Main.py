from functools import reduce
from operator import mul


def cmb(n, r):
    r = min(n - r, r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under

def main():
    n,p = map(int,input().split())
    a = list(map(int,input().split()))
    odd = 0
    total = 2 ** (len(a))
    odds = []
    ans = 0
    for num in a:
        if num % 2 == 1:
            odds.append(num)
    even = len(a) - len(odds)
    for i in range(len(odds) + 1):
        if i % 2 == 0:
            continue
        else:
            ans += cmb(len(odds), i) * pow(2, even)
    if p == 0:
        print(total - ans)
    else:
        print(ans)


if __name__ == '__main__':
    main()