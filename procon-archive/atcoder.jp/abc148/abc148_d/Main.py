if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))

    target = 1
    for i in range(len(a)):
        if a[i] == target:
            target += 1
        else:
            continue
    if 1 not in a:
        print(-1)
        exit()
    else:
        print(len(a) - (target -1))