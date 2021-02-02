from itertools import accumulate

if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    a_sum = list(accumulate(a))
    ans = float('inf')
    for i in range(n):
        r = a_sum[i]
        l = a_sum[n-1] - r
        ans = min(ans, abs(r-l))
    print(ans)