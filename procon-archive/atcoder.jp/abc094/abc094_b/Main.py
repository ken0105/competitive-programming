if __name__ == '__main__':
    n,m,x = map(int,input().split())
    a = set(map(int,input().split()))
    cost1 = 0
    cost2 = 0
    now = x
    while now != n and now != 0:
        now -= 1
        if now in a:
            cost1 += 1

    now = x
    while now != n and now != 0:
        now += 1
        if now in a:
            cost2 += 1
    print(min(cost1,cost2))





