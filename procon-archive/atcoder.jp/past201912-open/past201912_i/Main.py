def main():
    n, m = map(int, input().split())
    s,c = [], [],
    for _ in range(m):
        x,y = map(str, input().split())
        s.append(x)
        c.append(int(y))
    dp = [[float('inf')] * (m + 1) for _ in range(2 ** n)]
    dp[0][0] = 0
    for i in range(m):
        p = s[i]
        pattern = 0
        for index, j in enumerate(p[::-1]):
            if j == "Y":
                pattern = pattern | 2 ** index
        for k in range(2 ** n):
            dp[k][i + 1] = min(dp[k][i+1], dp[k][i])
            dp[k | pattern][i + 1] = min(dp[k | pattern][i + 1], dp[k][i] + c[i])

    ans = dp[2 ** n - 1][m]
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)







if __name__ == '__main__':
    main()
