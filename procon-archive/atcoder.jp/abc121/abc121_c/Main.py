if __name__ == '__main__':
    n,m = map(int,input().split())
    l = []
    for _ in range(n):
        a,b = map(int,input().split())
        l.append((a,b))
    l.sort()
    total = 0
    for a,b in l:
        if m >= b:
            m -= b
            total += a* b
        else:
            total += a* m
            m = 0

        if m == 0:
            break
    print(total)

