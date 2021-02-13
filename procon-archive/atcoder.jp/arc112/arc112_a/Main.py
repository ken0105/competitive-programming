def main():
    n = int(input())
    for i in range(n):
        l,r = map(int,input().split())
        if l * 2 > r:
            print(0)
            continue
        num = r - 2 * l + 1
        print((1 + num) * num // 2)


if __name__ == '__main__':
    main()