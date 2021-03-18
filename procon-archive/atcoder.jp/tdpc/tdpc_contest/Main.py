def main():
    N = int(input())
    ps = [0] + list(map(int, input().split()))

    P = sum(ps)

    exist = [[False] * (P + 1) for _ in range(N + 1)]
    exist[0][0] = True

    for i in range(1,N + 1):
        for j in range(P + 1):
            if exist[i-1][j]:
                exist[i][j] = True
            if exist[i-1][j - ps[i]]:
                exist[i][j] = True

    print(exist[N].count(True))

if __name__ == '__main__':
    main()