def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    lack = 0
    changed = 0
    amari = []
    for i in range(n):
        if b[i] > a[i]:
            changed += 1
            lack += b[i] - a[i]
        else:
            amari.append(a[i] - b[i])
    amari.sort()
    while lack > 0:
        try:
            lack -= amari.pop()
            changed += 1
        except:
            print(-1)
            exit()
    print(changed)

if __name__ == '__main__':
    main()