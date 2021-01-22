import bisect

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a.sort()
    b.sort()
    c.sort()

    ans = 0
    for i in b:
        a_num = bisect.bisect_left(a,i)
        c_num = bisect.bisect_right(c,i)
        ans += a_num * (len(c) - c_num)
    print(ans)