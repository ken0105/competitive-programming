def main():
    n, m = map(int, input().split())
    can_red = [False] * n
    kosu = [1] * n
    can_red[0] = True
    for _ in range(m):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        if can_red[x]:
            can_red[y] = True
        kosu[x] -= 1
        kosu[y] += 1
        if kosu[x] == 0:
            can_red[x] = False
    ans = sum([i for i in can_red])
    print(ans)



if __name__ == '__main__':
    main()
