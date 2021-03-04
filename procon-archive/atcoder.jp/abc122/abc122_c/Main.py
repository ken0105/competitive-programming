def main():
    n, q = map(int, input().split())
    s = input()
    now = 0
    cnt = [0] * n
    for i in range(n - 1):
        if s[i] + s[i+1] == "AC":
            now += 1
            cnt[i+1] = now
        else:
            cnt[i+1] = now
    for _ in range(q):
        l,r = map(int,input().split())
        print(cnt[r-1] - cnt[l-1])

if __name__ == '__main__':
    main()