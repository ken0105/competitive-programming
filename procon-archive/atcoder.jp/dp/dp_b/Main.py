import sys

input = sys.stdin.readline


def chmin(a, b):
    if a > b:
        return b
    else:
        return a


n, k = map(int, input().split())

h = list(map(int, input().split()))
dp = [float('inf')] * 10 ** 5
dp[0] = 0
for i in range(n - 1):
    for j in range(1, k + 1):
        if i + j < n:
            dp[i + j] = chmin(dp[i + j], dp[i] + abs(h[i + j] - h[i]))
print(dp[n-1])
