from collections import deque


def main():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        u, v = u - 1, v - 1
        g[u].append(v)
        g[v].append(u)

    s = int(input())
    s -= 1
    k = int(input())
    t = list(map(lambda x: int(x) - 1, input().split()))
    t = [s] + t
    k += 1
    dist = [[float('inf')] * k for i in range(k)]

    def bfs(sn):
        d = [float('inf') for _ in range(n)]
        d[sn] = 0
        queue = deque([sn])
        seen = set()
        while queue:
            q = queue.popleft()
            for i in g[q]:
                if i in seen:
                    continue
                seen.add(i)
                d[i] = min(d[q] + 1, d[i])
                queue.append(i)
        return d

    for i, sn in enumerate(t):
        distances = bfs(sn)
        for j, to in enumerate(t):
            dist[i][j] = distances[to]

    ALL = 1 << k
    dp = [[float('inf')] * k for _ in range(ALL)]
    dp[1][0] = 0

    for n in range(ALL):
        for i in range(k):
            for j in range(k):
                if (n >> j) & 1 or i == j:
                    continue
                dp[n | (1 << j)][j] = min(dp[n | (1 << j)][j], dp[n][i] + dist[i][j])
    print(min(dp[ALL - 1]))



if __name__ == '__main__':
    main()
