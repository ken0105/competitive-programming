def chmin(a,b):
    if a > b:
        return b
    else:
        return a

n = int(input())
h = list(map(int, input().split()))

dp = [1e50] * 10 ** 5
dp[0] = 0

for i in range(n-1):
    dp[i+1] = chmin(dp[i+1],dp[i] + abs(h[i] - h[i+1]))

    if i < n -2:
        dp[i +2] = chmin(dp[i+2], dp[i]+ abs(h[i] - h[i+2]))

print(dp[n-1])