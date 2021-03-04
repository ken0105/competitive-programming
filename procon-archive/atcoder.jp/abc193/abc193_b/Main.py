def main():
    n = int(input())
    ans = float('inf')
    for i in range(n):
        a,p,x = map(int,input().split())
        x -= a
        if x <= 0:
            continue
        else:
            ans = min(ans,p)
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()

