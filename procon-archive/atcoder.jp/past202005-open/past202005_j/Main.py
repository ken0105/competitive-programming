def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    eat = [0] * n
    for sushi in a:
        ok = -1
        ng = n
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if eat[mid] >= sushi:
                ok = mid
            else:
                ng = mid
        if ng == n:
            print(-1)
        else:
            eat[ok + 1] = sushi
            print(ok+2)



if __name__ == '__main__':
    main()
