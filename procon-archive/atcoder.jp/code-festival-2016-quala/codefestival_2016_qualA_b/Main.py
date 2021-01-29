if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    cnt = 0
    for i,num in enumerate(a):
        if a[a[i] - 1] - 1 == i:
            cnt += 1
    print(cnt//2)