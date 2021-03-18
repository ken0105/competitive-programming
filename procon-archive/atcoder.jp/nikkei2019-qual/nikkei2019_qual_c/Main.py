def main():
    n = int(input())
    l = []
    for i in range(n):
        a,b = map(int, input().split())
        l.append((a + b, a, b))
    l = sorted(l, key=lambda x: x[0], reverse=True)
    taka = 0
    aoki = 0
    for i in range(n):
        if i % 2 == 0:
            taka += l[i][1]
        else:
            aoki += l[i][2]
    print(taka - aoki)

if __name__ == '__main__':
    main()
