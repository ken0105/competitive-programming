def main():
    N, W = map(int, input().split())
    li = []
    for _ in range(N):
        w,v = map(int, input().split())
        li.append((w,v))

    dp = [[-1] * (W + 1) for _ in range(N + 1)]
    dp[0] = [0] * (W + 1)
    for i in range(N + 1):
        for j in range(W + 1):
            try:
                w,v = li[i]
                # 選ばない
                dp[i + 1][j] = max(dp[i][j], dp[i+1][j])
                # 選ぶ
                if j - w >= 0:
                    dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - w] + v)
            except:
                pass
    print(dp[N][W])




if __name__ == '__main__':
    main()
