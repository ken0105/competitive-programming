from heapq import heappop, heappush


def dijkstra(s, n, adj): # (始点, ノード数, 隣接リスト([ノード番号from][(ノード番号to, 距離)]))
    dist = [float('inf')] * n
    confirmed = [False] * n
    dist_candidate = [(0, s)] # 距離, 始点からの重み(距離)
    dist[s] = 0
    while dist_candidate:
        v = heappop(dist_candidate)[1] #確定させるノードを取得
        if confirmed[v]: #同一距離で確定済みだったら飛ばしていい
            continue
        confirmed[v] = True
        for to, weight in adj[v]:
            if not confirmed[to] and dist[to] > dist[v] + weight:
                dist[to] = dist[v] + weight
                heappush(dist_candidate, (dist[to], to))
    return dist

def main():
    n, e, s = map(int, input().split()) #ノード数(頂点の数), エッジ数, 始点ノード
    adj = [[] for _ in range(n)]
    for _ in range(e):
        n1, n2, w = map(int, input().split())
        adj[n1].append((n2, w))
    print(adj)
    print(dijkstra(s, n, adj))
    ans = dijkstra(s, n, adj)
    for i in ans:
        if i == float('inf'):
            print("INF")
        else:
            print(i)

if __name__ == "__main__":
    main()
