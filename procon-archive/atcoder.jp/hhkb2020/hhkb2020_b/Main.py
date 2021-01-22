if __name__ == "__main__":
    h, w = map(int, input().split())
    li = []
    count = 0
    for i in range(h):
        li.append(input())

    for i in range(h):
        for j in range(w):
            if i < h -1 and li[i][j] == "." and li[i + 1][j] == ".":
                count += 1
            if j >= w - 1:
                break
            if li[i][j] == "." and li[i][j + 1] == ".":
                count += 1
    print(count)
