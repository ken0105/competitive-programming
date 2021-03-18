def main():
    n, m, q = map(int, input().split())
    package = []
    for _ in range(n):
        w, v = map(int, input().split())
        package.append((w, v))
    x = list(map(int, input().split()))
    package = sorted(package, key=lambda x: x[1], reverse=True)
    # package = sorted(package, key=lambda x: x[0])
    for _ in range(q):
        l, r, = map(lambda x: int(x) - 1, input().split())
        box = []
        if r == m - 1:
            box = x[0:l]
        else:
            box = x[0:l] + x[r + 1:]
        if len(box) == 0:
            print(0)
            continue
        box.sort()
        ans = 0
        used = set()
        for b in box:
            for i,(w,v) in enumerate(package):
                if b >= w and i not in used:
                    ans += v
                    used.add(i)
                    break
        print(ans)




if __name__ == '__main__':
    main()
