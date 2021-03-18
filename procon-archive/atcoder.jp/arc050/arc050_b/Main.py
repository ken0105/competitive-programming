def main():
    r,b = map(int, input().split())
    x,y = map(int, input().split())
    ok = 0
    ng = 10 ** 18 + 1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid,r,b,x,y):
            ok = mid
        else:
            ng = mid
    print(ok)

def is_ok(mid, r,b,x,y):
    r -= mid
    b -= mid
    if r < 0 or b < 0:
        return False
    total = r // (x - 1)
    total += b // (y - 1)
    if total >= mid:
        return True
    else:
        return False






if __name__ == '__main__':
    main()
