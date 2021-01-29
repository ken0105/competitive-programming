if __name__ == '__main__':
    a,b,k = map(int,input().split())
    ans = set()
    for i in range(a,a+k):
        if i > b:
            break
        ans.add(i)

    for i in range(b,b-k,-1):
        if i < a:
            break
        ans.add(i)

    ans = list(ans)
    ans.sort()
    for a in ans:
        print(a)