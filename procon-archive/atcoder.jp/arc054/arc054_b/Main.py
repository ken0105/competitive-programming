if __name__ == '__main__':
    p = float(input())
    s = 0
    e = 100
    while abs(s - e) > 0.000000001:
        l1 = (s * 2 + e) / 3
        l2 = (s + e * 2) / 3
        t1 = l1 + p / (2 ** (l1 / 1.5))
        t2 = l2 + p / (2 ** (l2 / 1.5))
        if t1 > t2:
            s = l1
        else:
            e = l2
    print(s + p / (2 ** (s / 1.5)))
