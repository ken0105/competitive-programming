from itertools import accumulate

if __name__ == '__main__':
    K,N = map(int,input().split())
    d = [0] + [int(input()) for _ in range(K-1)]
    action = [int(input()) for _ in range(N)]
    accum_d = list(accumulate(d))
    now = 0
    ans = 0
    for a in action:
        ans += abs(accum_d[now+a] - accum_d[now])
        now = now + a
    print(ans % (10 ** 5))
