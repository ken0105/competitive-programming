def main():
    n, d , h = map(int, input().split())
    ans = 0
    for i in range(n):
        d1,h1 = map(int, input().split())
        x = d - d1
        y = h - h1
        ans = max(h1 - (d1*(y / x)), ans)
    print(max(ans,0))

if __name__ == '__main__':
    main()
