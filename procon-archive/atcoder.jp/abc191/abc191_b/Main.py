if __name__ == '__main__':
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    ans = []
    for num in a:
        if num != x:
            ans.append(num)
    print(*ans)