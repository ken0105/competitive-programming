def main():
    h, w = map(int, input().split())
    a = []
    for _ in range(h):
        a.append(input())
    route = [[0] * w for _ in range(h)]
    has_wall_w, has_wall_h = False, False
    for i in range(h):
        for j in range(w):
            if i == 0 and a[i][j] == "." and not has_wall_h:
                route[i][j] = 1
            elif i == 0 and a[i][j] == "#":
                has_wall_h = True
            elif j == 0 and a[i][j] == "." and not has_wall_w:
                route[i][j] = 1
            elif j == 0 and a[i][j] == "#":
                has_wall_w = True


    for i in range(1, h):
        for j in range(1, w):
            if a[i][j] == "#":
                continue
            route[i][j] = route[i - 1][j] + route[i][j - 1]
    print(route[h - 1][w - 1] % (10 ** 9 + 7))


if __name__ == '__main__':
    main()
