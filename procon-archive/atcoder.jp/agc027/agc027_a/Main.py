if __name__ == '__main__':
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    pre_x = x
    a.sort()
    ans = 0
    for i in a:
        if x - i >= 0:
            x -= i
            ans += 1
        else:
            break
    if sum(a) < pre_x:
        ans -= 1
    print(ans)
