import bisect

if __name__ == '__main__':
    n = int(input())
    h = []
    s = []
    for _ in range(n):
        x,y = map(int,input().split())
        h.append(x)
        s.append(y)

    def is_ok(penalty):
        s_list = []
        for i in range(n):
            s_list.append((penalty - h[i]) // s[i])
        s_list.sort()
        for i in range(n):
            if s_list[i] < i:
                return False
        return True

    def meguru_bisect(ng,ok):
        while abs(ng - ok) > 1:
            mid = (ng + ok) //2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    print(meguru_bisect(0, int(1e14)))

