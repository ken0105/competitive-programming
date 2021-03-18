from collections import deque


def main():
    h,w = map(int, input().split())
    c = [input() for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if c[i][j] == "s":
                si, sj = i, j
            if c[i][j] == "g":
                gi, gj = i, j

    seen = [[False] * w for _ in range(h)]

    stack = deque()
    stack.append((si,sj))
    while stack:
        i,j = stack.pop()
        seen[i][j] = True
        for i2, j2 in [[i+1,j], [i, j - 1], [i - 1, j],[i, j + 1]]:
            if not (0 <= i2 < h and 0 <= j2 < w):
                continue
            if c[i2][j2] == "#":
                continue
            if not seen[i2][j2]:
                stack.append((i2, j2))
    if seen[gi][gj]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()