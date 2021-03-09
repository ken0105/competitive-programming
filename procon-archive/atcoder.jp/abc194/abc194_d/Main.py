def main():
    n = int(input())
    ans = n
    ans2 = 0
    for i in range(n-1, 0, -1):
        ans2 += 1 / i
    print(ans * ans2)

if __name__ == '__main__':
    main()
