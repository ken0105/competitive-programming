def main():
    N,W = map(int, input().split())
    item = []
    sum_v = 0
    for _ in range(N):
        w,v = map(int, input().split())
        item.append((w,v))
        sum_v += v

    weight = [[float('inf')] * (sum_v + 1) for _ in range(N + 1)]
    weight[0][0] = 0

    for i in range(N):
        for j in range(sum_v + 1):
            weight[i+1][j] = min(weight[i+1][j], weight[i][j])
            if j - item[i][1] >= 0:
                weight[i + 1][j] = min(weight[i][j], weight[i][j - item[i][1]] + item[i][0])

    ans = 0
    for i in range(N+1):
        for j in range(sum_v + 1):
            if 0 <= weight[i][j] <= W:
                ans = max(ans, j)

    print(ans)






if __name__ == '__main__':
    main()
