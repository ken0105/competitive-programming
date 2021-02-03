if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))

    cnt = 0
    now = 0
    for i,num in enumerate(a):
        if now == 1:
            print(cnt)
            exit()
        else :
            now = a[now] - 1
            cnt += 1
    print(-1)