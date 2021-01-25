if __name__ == '__main__':
    n = int(input())
    d,x = map(int,input().split())
    ans = x
    for i in range(n):
        a = int(input())
        ans += 1
        day = 1
        while day + a <= d:
            ans += 1
            day += a
    print(ans)


