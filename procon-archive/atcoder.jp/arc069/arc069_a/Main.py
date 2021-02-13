def main():
    n,m = map(int, input().split())
    total = n * 2 + m
    print(min(total // 4, m // 2))

if __name__ == '__main__':
    main()