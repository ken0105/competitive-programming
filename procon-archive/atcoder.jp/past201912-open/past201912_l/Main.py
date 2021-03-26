import heapq
import math
from collections import deque


def main():
    n,m = map(int, input().split())
    xyc_large = [list(map(int, input().split())) for _ in range(n)]
    xyc_small = [list(map(int, input().split())) for _ in range(m)]

    def calc(xyz1,xyz2):
        x1,y1,c1 = xyz1[0], xyz1[1], xyz1[2]
        x2,y2,c2 = xyz2[0], xyz2[1], xyz2[2],
        dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if c1 != c2:
            dist *= 10
        return dist

    ans = float('inf')

    for bit in range(1 << m):
        use_towers = xyc_large[:]
        for i in range(m):
            if bit >> i & 1:
                use_towers.append(xyc_small[i])
        que = []
        heapq.heappush(que,(0.0, 0))
        used = set()
        total = 0
        while que:
            cost, p = heapq.heappop(que)
            if p in used:
                continue
            total += cost
            used.add(p)
            for i in range(len(use_towers)):
                if i not in used:
                    dist = calc(use_towers[p], use_towers[i])
                    heapq.heappush(que, (dist, i))
        ans = min(total, ans)
    print(ans)
if __name__ == '__main__':
    main()
