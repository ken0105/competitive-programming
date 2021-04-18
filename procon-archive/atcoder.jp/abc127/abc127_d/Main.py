def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    l = []
    for _ in range(m):
        b,c = map(int, input().split())
        l.append((c,b))
    l.sort()
    for i, num, in enumerate(a):
        if l:
            c,b = l.pop()
        else:
            break
        if num > c:
            break
        else:
            a[i] = c
            b -= 1
            if b != 0:
                l.append((c,b))
    print(sum(a))


if __name__ == '__main__':
    main()
