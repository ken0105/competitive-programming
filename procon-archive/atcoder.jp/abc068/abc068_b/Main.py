import math

if __name__ == '__main__':
    n = int(input())
    ans = 1
    while ans <= n:
        if ans == n:
            print(n)
            exit()
        if ans * 2 > n:
            print(ans)
            exit()
        ans *= 2


