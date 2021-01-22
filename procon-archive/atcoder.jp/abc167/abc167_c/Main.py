if __name__ == '__main__':
    n, m, x = map(int, input().split())
    li = [list(map(int, input().split())) for i in range(n)]
    ans = float('inf')
    for bit in range(2 ** n):
        exp = [0] * (n + 1)
        for i in range(n):
            if bit >> i & 1:
                exp = [x + y for (x,y) in zip(exp,li[i])]

        ok = True
        for i in range(1,len(exp)):
            if exp[i] < x:
                ok = False
        if ok:
            ans = min(ans, exp[0])
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)
