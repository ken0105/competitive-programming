import sys
sys.setrecursionlimit(1000000)
ans = 0


def main():
    H, W, a, b = map(int, input().split())

    def dfs(i, bit, a, b):
        global ans
        if i == H * W:
            ans += 1
            return
        h, w = divmod(i, W)
        if (bit >> i) & 1:
            dfs(i + 1, bit, a, b)
            return
        if b > 0:
            dfs(i + 1, bit | (1 << i), a, b - 1)
        if a > 0:
            if not (bit >> (i + 1)) & 1 and w + 1 < W:
                dfs(i + 2, bit | (1 << i) | (1 << (i + 1)), a - 1, b)
            if not (bit >> (i + W)) & 1 and h + 1 < H:
                dfs(i + 1, bit | (1 << i) | (1 << (i + W)), a - 1, b)

    dfs(0, 0, a, b)
    global ans
    print(ans)


if __name__ == '__main__':
    main()
