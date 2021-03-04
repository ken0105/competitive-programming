import math


def main():
    n,m,k = map(int,input().split())
    can = set()
    for row in range(n+1):
        for column in range(m+1):
            num = m * row + n * column - (row * column) * 2
            can.add(num)
    if k in can:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
