def Base_n_to_10(X,n):
    out = 0
    for i in range(1,len(str(X))+1):
        out += int(X[-i])*(n**(i-1))
    return out


def main():
    x = input()
    m = int(input())
    if len(x) == 1:
        if int(x) > m:
            print(0)
        else:
            print(1)
        exit()
    def __is_ok(target, m):
        if Base_n_to_10(x, target) <= m:
            return True
        else:
            return False

    ok = int(max(list(x)))
    ng = 10 ** 18 + 100
    while abs(ok-ng) > 1:
        mid = (ok + ng) // 2
        is_ok = __is_ok(mid,m)
        if is_ok:
            ok = mid
        else:
            ng = mid
    print(ok - int(max(list(x))))




if __name__ == '__main__':
    main()


class BinarySearch:
    def __init__(self, l, target):
        self.l = l
        self.target = target

    def __is_ok(self, mid):
        return True

    def bisect(self):
        ok = -1
        ng = len(self.l)
        while abs(ok-ng) > 1:
            mid = (ok+ng) // 2
            is_ok = self.__is_ok(mid)
            if is_ok:
                ok = mid
            else:
                ng = mid
        return ok
