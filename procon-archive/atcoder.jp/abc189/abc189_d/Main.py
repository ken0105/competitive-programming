if __name__ == '__main__':
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())

    dp = [[0, 0]] * (n + 1)
    dp[0] = [1, 1]
    for i in range(1, n + 1):
        if s[i - 1] == "AND":
            dp[i] = [dp[i-1][0], dp[i-1][1] * 2 + dp[i-1][0]]
        else:
            t = dp[i-1][0] * 2 + dp[i-1][1]
            f = dp[i-1][1]
            dp[i] = [t,f]
    print(dp[n][0])
