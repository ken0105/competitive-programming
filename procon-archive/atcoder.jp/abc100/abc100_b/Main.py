if __name__ == '__main__':
    d,n, = map(int,input().split())
    cnt = 0
    for i in range(n*2):
        if d == 0 and 100 ** d * i % 100 == 0:
            continue
        elif d == 1 and 100 ** d * i % 10000 == 0:
            continue
        elif d == 2 and 100 ** d * i % 1000000 == 0:
            continue
        cnt += 1
        if cnt == n:
            print(100 ** d * i)
            exit()
