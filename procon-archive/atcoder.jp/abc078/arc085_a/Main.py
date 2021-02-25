def main():
    n,m = map(int,input().split())
    try_cnt = 2 ** m
    ans = (1900 * m + 100 * (n - m)) * try_cnt
    print(ans)

if __name__ == '__main__':
    main()
