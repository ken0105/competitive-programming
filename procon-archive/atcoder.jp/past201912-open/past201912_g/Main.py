def main():
    n = int(input())
    a = []
    for i in range(n-1):
        a.append([0] * (i + 1) + list(map(int, input().split())))

    pattern = 2 ** n
    happy = [[] for _ in range(pattern)]
    for i in range(pattern):
        num = 0
        for j in range(n):
            for k in range(j+1, n):
                if i >> j & 1 and i >> k & 1:
                    num += a[j][k]
        happy[i] = num

    ans = -(10 ** 10)
    for i in range(pattern):
        for j in range(pattern):
            if i & j != 0:
                continue
            k = (pattern - 1) - (i | j)
            ans = max(ans, happy[i] + happy[j] + happy[k])
    print(ans)


if __name__ == '__main__':
    main()
