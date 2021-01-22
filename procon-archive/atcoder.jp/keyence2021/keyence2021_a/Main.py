if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    max_a = []
    a_max = 0
    max_b = []
    b_max = 0
    for i in range(n):
        a_max = max(a_max,a[i])
        b_max = max(b_max,b[i])
        max_a.append(a_max)
        max_b.append(b_max)
    max_b = max_b[::-1]
    ans = 0
    for i in range(n):
        ans = max(ans, max_a[i] * b[i])
        print(ans)