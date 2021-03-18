def main():
    n,m = map(int, input().split())
    a = [input() for _ in range(n)]

    group = [[] for _ in range(11)]
    for i in range(n):
        for j in range(m):
            if a[i][j] == "S":
                group[0].append((i,j))
                si,sj = i,j
            elif a[i][j] == "G":
                group[10].append((i,j))
                gi,gj = i,j
            else:
                group[int(a[i][j])].append((i,j))

    dp = [[float('inf')] * m for _ in range(n)]
    dp[si][sj] = 0
    for i in range(1,11):
        before = group[i - 1]
        after = group[i]
        for i,j in before:
            for i2,j2 in after:
                dp[i2][j2] = min(dp[i2][j2], dp[i][j] + abs(i2 - i) + abs(j2 - j))

    if dp[gi][gj] == float('inf'):
        print(-1)
    else:
        print(dp[gi][gj])

if __name__ == '__main__':
    main()
