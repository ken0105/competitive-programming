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

