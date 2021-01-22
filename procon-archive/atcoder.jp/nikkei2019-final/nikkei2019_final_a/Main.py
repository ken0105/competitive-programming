from itertools import accumulate

if __name__ == '__main__':
    n = int(input())
    A = [0] + list(map(int,input().split()))
    csum = list(accumulate(A))

    for k in range(1,n+1):
        ans = 0
        for i in range(n+1):
            if i - k >= 0:
                ans = max(csum[i] - csum[i-k], ans)
        print(ans)
