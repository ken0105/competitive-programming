def main():
    n = int(input())
    l = [list(map(int, input().split())) for _ in range(n)]

    ok = 1
    ng = 1e10
    def is_ok(x):
        binary = [False] * (1 << 5)
        for spec in l:
            param = 0
            for i in range(5):
                if spec[i] >= x:
                    param = param | (1 << i)
            binary[param] = True
        for i in range(1<<5):
            for j in range(1<<5):
                for k in range(1<<5):
                    if ((i | j | k) == (1 << 5) - 1) and binary[i] and binary[j] and binary[k]:
                        return True
        return False


    while abs(ok - ng ) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid

    print(int(ok))





if __name__ == '__main__':
    main()
