if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    min_a = min(a)
    max_a = max(a)
    ans = float('inf')
    for i in range(min_a,max_a+1):
        total = 0
        for j in a:
            total += (i - j) ** 2
        ans = min(ans,total)
    print(ans)