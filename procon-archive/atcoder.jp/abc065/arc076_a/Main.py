import math
import sys


def fact(x,total):
    while x > 1:
        total = total * x % (10 ** 9 + 7)
        x -= 1
    return total

def main():
    n, m = map(int, input().split())
    if abs(n-m) >= 2:
        print(0)
        exit()
    ans = fact(n,1) * fact(m,1)
    if abs(n-m) == 1:
        print(ans % (10 ** 9 + 7))
    else:
        print(ans * 2 % (10 ** 9 + 7))

if __name__ == '__main__':
    main()
