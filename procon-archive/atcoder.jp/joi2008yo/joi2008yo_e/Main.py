def main():
    r,c = map(int, input().split())
    s = [list(map(int, input().split())) for _ in range(r)]
    h = [0] * c
    for i in range(r):
        for j in range(c):
            if s[i][j] == 1:
                h[j] += 1
    ans = 0
    for bit in range(1 << r):
        heads = h[:]
        for i in range(r):
            if bit >> i & 1:
                for j in range(c):
                    if s[i][j] == 0:
                        heads[j] += 1
                    else:
                        heads[j] -= 1
        cnt = 0
        for j in range(c):
            cnt += max(heads[j], r - heads[j])
        ans = max(ans, cnt)
    print(ans)


if __name__ == '__main__':
    main()
