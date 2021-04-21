import math


def main():
    a,b = map(int, input().split())
    for i in range(10 ** 5 * 2 + 1, 0, -1):
        if a <= math.ceil(a / i) * i <= b and a <= math.ceil(a / i) * i + i <= b:
            print(i)
            exit()
        else:
            continue

if __name__ == '__main__':
    main()
