if __name__ == '__main__':
    x, k, d = map(int, input().split())
    x = abs(x)
    c = x // d
    rest = k - c
    ans = 0
    if rest % 2 == 0:
        ans = x - (d * c)
    else:
        ans = x - (d * (c + 1))

    if x - (k * d) > 0:
        ans = x - (k * d)
    print(abs(ans))