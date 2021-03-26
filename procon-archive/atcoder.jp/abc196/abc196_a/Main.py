def main():
    a,b = map(int, input().split())
    c,d = map(int, input().split())
    ans = -float('inf')
    for i in range(a,b+1):
        for j in range(c,d+1):
            ans = max(ans, (i-j))
    print(ans)

if __name__ == '__main__':
    main()
