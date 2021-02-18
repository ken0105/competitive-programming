def main():
    w, h, n = map(int,input().split())
    x_from = 0
    x_to = w
    y_from = 0
    y_to = h
    for _ in range(n):
        x, y, a = map(int, input().split())
        if a == 1:
            x_from = max(x_from, x)
        if a == 2:
            x_to = min(x_to, x)
        if a == 3:
            y_from = max(y_from, y)
        if a == 4:
            y_to = min(y_to, y)
        if x_from > x_to:
            x_from = x_to
        if y_from > y_to:
            y_from = y_to
    print((x_to - x_from) * (y_to - y_from))


if __name__ == '__main__':
    main()