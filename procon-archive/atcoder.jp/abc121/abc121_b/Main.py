if __name__ == '__main__':
    n,m,c = map(int,input().split())
    b = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        a = list(map(int,input().split()))
        total = c
        for x,y in zip(a,b):
            total += x * y
        if total > 0:
            ans += 1
    print(ans)