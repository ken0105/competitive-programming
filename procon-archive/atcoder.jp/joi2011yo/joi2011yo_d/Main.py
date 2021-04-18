def main():
    n = int(input())
    n -= 1
    l = list(map(int, input().split()))
    a = l.pop()
    dp = [[0] * n for _ in range(21)]
    dp[l[0]][0] = 1
    for i in range(1,n):
        for j in range(21):
            num = l[i]
            if dp[j][i-1] > 0 and j + num <= 20:
                dp[j+num][i] += dp[j][i-1]
            if dp[j][i-1] > 0 and j - num >= 0:
                dp[j-num][i] += dp[j][i-1]
    print(dp[a][n-1])
if __name__ == '__main__':
    main()
