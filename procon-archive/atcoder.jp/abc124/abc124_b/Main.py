def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    height = 0
    for i in range(n):
        if height <= h[i]:
            ans += 1
            height = h[i]
    print(ans)

if __name__ == '__main__':
    main()
