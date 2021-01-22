import sys


def solve():
    global list
    input = sys.stdin.readline
    mod = pow(10, 9) + 7
    N = input()
    list = list(map(int, input().split()))

    squere = sum(list) ** 2
    diag = 0

    for i in list:
        diag += i ** 2

    print(int((squere - diag) // 2 % mod))

    return 0


if __name__ == "__main__":
    solve()
