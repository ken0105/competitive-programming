from heapq import heappop, heappush

def dijkstra(s,n, adj):
    dist = [float('inf')] * n
    confirmed = [False] * n
    dist_candidate = [(0, s)]
    dist[s] = 0
    while dist_candidate:
        v = heappop(dist_candidate)[1]
        if confirmed[v]:
            continue
        confirmed[v] = True
        for to, weight in adj[v]:
            if not confirmed[to] and dist[to] > dist[v] + weight:
                dist[to] = dist[v] + weight
                heappush(dist_candidate, (dist[to], to))
    return dist

def main():
    n, k = map(int, input().split())
    n += 1
    adj = [[] for _ in range(n)]
    for i in range(k):
        num, *li = map(int, input().split())
        if num == 0:
            ans = dijkstra(li[0], n, adj)
            if ans[li[1]] == float('inf'):
                print(-1)
            else:
                print(ans[li[1]])
        else:
            adj[li[0]].append((li[1], li[2]))
            adj[li[1]].append((li[0], li[2]))



if __name__ == '__main__':
    main()
