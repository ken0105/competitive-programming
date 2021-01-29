if __name__ == '__main__':
    q,h,s,d = map(int,input().split())
    n = int(input())
    q1 = q * 4
    h1 = h * 2
    s1 = s

    ans = float('inf')
    ans = min(ans, n * q1)
    ans = min(ans, n * h1)
    ans = min(ans, n * s1)
    if n % 2 == 0:
        ans = min(ans, (n // 2) * d)
    else:
        min_size = min(q1, h1)
        min_size = min(min_size, s1)
        ans = min(ans, (n // 2) * d + min_size)
    print(int(ans))