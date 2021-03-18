def main():
    n = int(input())
    x = [[] for _ in range(n + 1)]
    for _ in range(n):
        a, b = map(int, input().split())
        x[a].append(b)

    cnt = [0] * 101
    ans = 0
    for i in range(1,n + 1):
        for b in x[i]:
            cnt[b] += 1

        for p in range(100, 0, -1):
            if cnt[p] != 0:
                cnt[p] -= 1
                ans += p
                print(ans)
                break






if __name__ == '__main__':
    main()
