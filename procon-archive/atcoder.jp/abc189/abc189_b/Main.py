if __name__ == '__main__':
    n,x = map(int,input().split())
    total = 0
    x *= 100
    for i in range(n):
        v,p = map(int,input().split())
        al = v * p
        total += al
        if total > x:
            print(i+1)
            exit()
    print(-1)