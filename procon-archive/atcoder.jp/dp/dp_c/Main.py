import sys

input = sys.stdin.readline


def chmax(a, b):
    if a > b:
        return a
    else:
        return b


n = int(input())
li = [list(map(int, input().split())) for i in range(n)]


dp = [list(0 for i in range(3)) for j in range(n + 1)]

for i in range(n):
    for j in range(3):
        for k in range(3):
            if j != k:
                dp[i + 1][j] = chmax(dp[i + 1][j], dp[i][k] + li[i][j])
max = max(dp[i + 1][0],dp[i + 1][1],dp[i + 1][2])
print(max)
