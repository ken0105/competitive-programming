def main():
    k,a,b = map(int,input().split())
    if b - a <= 1:
        print(k + 1)
        exit()

    if a >= k:
        print(k + 1)
        exit()

    rest = k - a - 1
    ans = b
    if rest % 2 == 0:
        ans += (b-a) * (rest // 2)
    else:
        ans += (b-a) * (rest // 2) + 1

    print(ans)
if __name__ == '__main__':
    main()
