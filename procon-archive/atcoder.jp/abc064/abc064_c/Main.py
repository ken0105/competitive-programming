if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    colors = set()
    top = 0
    for score in a:
        color = score // 400
        if color < 8:
            colors.add(color)
            continue
        top += 1

    min_color = len(colors)
    if top != 0 and min_color == 0:
        min_color += 1
    max_color = len(colors) + top
    print(min_color, max_color)

