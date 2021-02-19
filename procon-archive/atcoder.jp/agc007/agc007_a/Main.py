def main():
    h,w = map(int, input().split())
    road = [input() for _ in range(h)]
    cnt = 0
    for row in range(h):
        for column in range(w):
            if road[row][column] == "#":
                cnt += 1
    if cnt == h + w - 1:
        print("Possible")
    else:
        print("Impossible")

if __name__ == '__main__':
    main()