from heapq import heappop, heappush

def dijkstra(s, n, adj): # (始点, ノード数, 隣接リスト([ノード番号from][(ノード番号to, 距離)]))
    dist = [float('inf')] * n
    confirmed = [False] * n
    dist_candidate = [(0, s)] #距離, ノード番号
    dist[s] = 0
    while dist_candidate:
        v = heappop(dist_candidate)[1]
        if confirmed[v]:
            continue
        confirmed[v] = True
        for to, weight, k in adj[v]:
            wait = 0
            if dist[v] % k != 0:
                wait = k - dist[v] % k
            if not confirmed[to] and dist[to] > (dist[v] + weight) + wait:
                dist[to] = (dist[v] + weight) + wait
                heappush(dist_candidate, (dist[to], to))
    return dist

def main():
    n, e, s, fin = map(int, input().split()) #ノード数, エッジ数, 始点ノード
    s -= 1
    fin -= 1
    adj = [[] for _ in range(n)]
    for _ in range(e):
        n1, n2, w, k = map(int, input().split())
        n1 -= 1
        n2 -= 1
        adj[n1].append((n2, w, k)) # 行き先ノード, 重み, タイミング
        adj[n2].append((n1, w, k))
    ans = dijkstra(s, n, adj)
    if ans[fin] == float('inf'):
        print(-1)
    else:
        print(ans[fin])

if __name__ == "__main__":
    main()
