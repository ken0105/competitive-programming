if __name__ == '__main__':
    n, a, b = map(int, input().split())
    if n == 2 and a <= b:
        print(1)
        exit()
    if n == 1 and a == b:
        print(1)
        exit()
    if n == 1 and a != b:
        print(0)
        exit()

    if a > b:
        print(0)
        exit()

    dist = ((a + b) + (n - 2) * b) - ((a+b) + (n -2) * a) + 1
    print(dist)
