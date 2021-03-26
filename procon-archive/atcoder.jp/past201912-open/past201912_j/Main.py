import heapq


def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]

    def dijkstra(si, sj):
        dist = [[float('inf')] * w for _ in range(h)]
        dist[si][sj] = 0
        que = []
        heapq.heapify(que)
        heapq.heappush(que,[0, si,sj])
        while que:
            d,i,j = heapq.heappop(que)
            for i2,j2 in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0 <= i2 < h and 0 <= j2 < w and dist[i2][j2] > d + a[i2][j2]:
                    dist[i2][j2] = d + a[i2][j2]
                    heapq.heappush(que, (dist[i2][j2], i2,j2))
        return dist

    dist1 = dijkstra(h-1, 0)
    dist2 = dijkstra(h-1, w-1)
    dist3 = dijkstra(0,w-1)
    ans = float('inf')
    for i in range(h):
        for j in range(w):
            res = dist1[i][j] + dist2[i][j] + dist3[i][j] - a[i][j] * 2
            ans = min(res,ans)
    print(ans)

if __name__ == '__main__':
    main()
