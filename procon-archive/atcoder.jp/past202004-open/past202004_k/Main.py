def main():
    n = int(input())
    s = " " + input()
    c = [0] + list(map(int, input().split()))
    d = [0] + list(map(int, input().split()))

    cost = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    cost[0] = [0] * (n+1)
    for i in range(n):
        for j in range(n):
            if j > i:
                continue
            if s[i+1] == "(":
                cost[i+1][j+1] = min(cost[i+1][j+1], cost[i][j])
                cost[i+1][j-1] = min(cost[i+1][j-1], cost[i][j] + c[i+1])
            else:
                cost[i+1][j-1] = min(cost[i+1][j-1], cost[i][j])
                cost[i+1][j+1] = min(cost[i+1][j+1], cost[i][j] + c[i+1])
            cost[i+1][j] = min(cost[i+1][j],cost[i][j] + d[i+1])


    print(cost[n][0])
if __name__ == '__main__':
    main()
