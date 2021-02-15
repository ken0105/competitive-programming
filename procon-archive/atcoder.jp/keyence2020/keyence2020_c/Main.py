import math


def main():
    n,k,s = map(int,input().split())
    a = []
    while True:
        if len(a) == k:
            break
        a.append(s)
    while True:
        if len(a) == n:
            break
        if s != 10 ** 9:
            a.append(10 ** 9)
        else:
            a.append(10 ** 9 - 1)
    print(*a)

if __name__ == '__main__':
    main()