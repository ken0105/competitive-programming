def main():
    a,r,n = map(int, input().split())
    if r == 1:
        print(a)
        exit()
    for i in range(n-1):
        a *= r
        if a > 10 ** 9:
            print("large")
            exit()
    print(a)


if __name__ == '__main__':
    main()
