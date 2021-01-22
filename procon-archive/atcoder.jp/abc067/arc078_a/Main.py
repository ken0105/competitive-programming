if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    sum_a = sum(a)
    arai = sum_a
    snuke = 0
    ans = float('inf')
    for i in a[0:n-1]:
        snuke += i
        arai -= i
        ans = min(ans,abs(snuke- arai))
    print(ans)