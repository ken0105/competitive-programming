g = []
start = [0]
end = [0]
now = 0

import sys
sys.setrecursionlimit(1000000)

def main():
    n = int(input())
    global g
    g = [[] for _ in range(n)]
    r = -1
    for i in range(n):
        p = int(input())
        if p == -1:
            r = i
        else:
            g[p - 1].append(i)
    global start, end
    start = [0] * n
    end = [0] * n
    dfs(g, r)
    q = int(input())
    for _ in range(q):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        if start[b] < start[a] < end[b]:
            print("Yes")
        else:
            print("No")


def dfs(g, i):
    global now, start, end
    now += 1
    start[i] = now
    for p in g[i]:
        dfs(g, p)
    now += 1
    end[i] = now


if __name__ == '__main__':
    main()
