import sys


def solve():
    input = sys.stdin.readline
    S = input()
    T = input()
    t_len = len(T)
    diff_c = 0
    needchange = 1000

    for i in range(len(S) - t_len + 1):
        for j in range(t_len - 1):
            if S[i + j] != T[j]:
                diff_c += 1
        if needchange > diff_c:
            needchange = diff_c
        diff_c = 0

    print(needchange)

    return 0


if __name__ == "__main__":
    solve()
