def main():
    n, m = map(int, input().split())
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    ans = list((a - b) | (b - a))
    ans.sort()
    print(*ans)


if __name__ == '__main__':
    main()
