import math


def main():
    x,y,z, = map(int, input().split())
    ans = 1
    for i in range(10 ** 6 + 1):
        if ans / z < y / x:
            ans += 1
        else:
            print(ans - 1)
            exit()

if __name__ == '__main__':
    main()
