def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [float('inf')] * n
    dp[0] = 0
    for i in range(n-1):
        dp[i+1] = min(dp[i+1], dp[i] + abs(a[i] - a[i+1]))
        if i + 2 <= n - 1:
            dp[i+2] = min(dp[i+2], dp[i] + abs(a[i] - a[i+2]))
    print(dp[n-1])

if __name__ == '__main__':
    main()
