from bisect import bisect, bisect_right, bisect_left

if __name__ == "__main__":
    n,m = map(int,input().split())
    a = set()
    for i in range(m):
        a.add(int(input()))

    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1,n+1):
        if i not in a and i >= 2:
            dp[i] = (dp[i-1] + dp[i-2])
        elif i not in a and i == 1:
            dp[i] = dp[i-1]
    print(dp[n] % 1000000007)