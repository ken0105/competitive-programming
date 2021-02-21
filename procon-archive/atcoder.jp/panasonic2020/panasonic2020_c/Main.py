from math import sqrt


def main():
    a, b, c = map(int, input().split())
    if c - b - a > 0 and 4 * a * b < (c - b - a) ** 2:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
