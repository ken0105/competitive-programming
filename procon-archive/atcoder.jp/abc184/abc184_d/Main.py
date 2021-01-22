
if __name__ == '__main__':
    a, b, c = map(int, input().split())
    dp = [[[0] * 101 for _ in range(101)] for _ in range(101)]
    dp[a][b][c] = 1
    ans = 0
    for i in range(a, 101):
        for j in range(b, 101):
            for k in range(c, 101):
                if i == 100 or j == 100 or k == 100:
                    ans += dp[i][j][k] * (i + j + k - (a + b + c))
                    continue
                dp[i + 1][j][k] += dp[i][j][k] * (i / (i + j + k))
                dp[i][j + 1][k] += dp[i][j][k] * (j / (i + j + k))
                dp[i][j][k + 1] += dp[i][j][k] * (k / (i + j + k))
    ans = format("%.10f" % ans)
    print(ans)
