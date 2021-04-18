def main():
    n,m = map(int, input().split())
    a = [input() for _ in range(n)]
    b = [input() for _ in range(m)]
    for i in range(n-m+1):
        for j in range(n-m+1):
            ok = True
            for k in range(m):
                x = a[i+k][j:j+m]
                y = b[k]
                if x != y:
                    ok = False
                    break
            if ok:
                print("Yes")
                exit()
    print("No")
    exit()

if __name__ == '__main__':
    main()
