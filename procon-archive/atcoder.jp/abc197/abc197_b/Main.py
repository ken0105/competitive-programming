def main():
    h,w,x,y = map(int, input().split())
    x -= 1
    y -= 1
    s = [input() for _ in range(h)]
    if s[x][y] == "#":
        print(0)
        exit()

    ans = 0
    now_x = x - 1
    while now_x >= 0:
        if s[now_x][y] == ".":
            ans += 1
        else:
            break
        now_x -= 1

    now_x = x + 1
    while now_x < h:
        if s[now_x][y] == ".":
            ans += 1
        else:
            break
        now_x += 1

    now_y = y - 1
    while now_y >= 0:
        if s[x][now_y] == ".":
            ans += 1
        else:
            break
        now_y -= 1

    now_y = y + 1
    while now_y < w:
        if s[x][now_y] == ".":
            ans += 1
        else:
            break
        now_y += 1

    if s[x][y] == ".":
        ans += 1

    print(ans)




if __name__ == '__main__':
    main()
