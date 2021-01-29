if __name__ == '__main__':
    n, k, = map(int, input().split())
    h = []
    for i in range(n):
        h.append(int(input()))
    h.sort()

    ans = float('inf')
    for i in range(n):
        if i + k - 1 >= n:
            break
        ans = min(ans, abs(h[i] - h[i+k-1]))
    print(ans)