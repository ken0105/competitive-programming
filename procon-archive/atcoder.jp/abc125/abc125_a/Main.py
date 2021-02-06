if __name__ == '__main__':
    A,B,T = map(int,input().split())
    now = 0
    ans = 0
    while now + A < T + 0.5:
        now += A
        ans += B
    print(ans)