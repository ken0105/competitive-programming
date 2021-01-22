import itertools

if __name__ == '__main__':
    n,x = map(int,input().split())
    l = list(map(int,input().split()))
    cnt = 1
    d = 0
    for i in l:
        d += i
        if d <= x:
            cnt += 1
        else:
            break
    print(cnt)