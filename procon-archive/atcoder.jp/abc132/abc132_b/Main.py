if __name__ == '__main__':
    n = int(input())
    p = list(map(int,input().split()))
    cnt = 0
    for i in range(n):
        if i + 1 > n -1 or i - 1 < 0:
            continue
        if p[i+1] > p[i] > p[i-1] or p[i+1] < p[i] < p[i-1]:
            cnt += 1
    print(cnt)