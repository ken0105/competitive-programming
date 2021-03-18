def main():
    n,l = map(int, input().split())
    x = set(map(int, input().split()))
    t1, t2, t3 = map(int, input().split())
    dp = [float('inf') for _ in range(l + 1)]
    dp[0] = 0
    for i in range(l):
        try:
            if i not in x:
                dp[i + 1] = min(dp[i+1], dp[i] + t1)
                dp[i + 2] = min(dp[i+2], dp[i] + t1 + t2)
                dp[i + 4] = min(dp[i+4], dp[i] + t1 + t2 * 3)
            else:
                dp[i + 1] = min(dp[i+1], dp[i] + t1 + t3)
                dp[i + 2] = min(dp[i+2], dp[i] + t1 + t2 + t3)
                dp[i + 4] = min(dp[i+4], dp[i] + t1 + t2 * 3 + t3)
        except:
            pass

    for i in range(1,4):
        try:
            if l - i not in x:
                dp[l] = min(dp[l], dp[l-i] + t1 * 0.5 + (0.5 + i - 1) * t2)
            else:
                dp[l] = min(dp[l], dp[l-i] + t1 * 0.5 + (0.5 + i - 1) * t2 + t3)
        except:
            pass

    print(int(dp[l]))


if __name__ == '__main__':
    main()