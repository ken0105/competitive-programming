def main():
    n,m = map(int, input().split())
    cost = []
    can_open = []
    for _ in range(m):
        a,b = map(int, input().split())
        c = list(map(lambda x: int(x) - 1, input().split()))
        cost.append(a)
        key_pattern = 0
        for k in c:
            key_pattern = key_pattern | 2 ** k
        can_open.append(key_pattern)

    pattern = 2 ** n
    dp = [[float('inf')] * pattern for _ in range(m + 1)]
    dp[0][0] = 0
    for i in range(m):
        for p in range(pattern):
            dp[i + 1][p] = min(dp[i][p], dp[i + 1][p])
            dp[i + 1][p | can_open[i]] = min(dp[i+1][p | can_open[i]], dp[i][p] + cost[i])

    if dp[m][pattern - 1] == float('inf'):
        print(-1)
    else:
        print(dp[m][pattern - 1])


if __name__ == '__main__':
    main()
