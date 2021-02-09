if __name__ == '__main__':
    n,k = map(int,input().split())
    ans = 0
    for i in range(1,n+1):
        p = 1 / n
        while i < k:
            i *= 2
            p /= 2
        ans += p
    print(ans)

