if __name__ == '__main__':
    n,m = map(int,input().split())
    ab = [map(int,input().split()) for _ in range(n)]
    cd = [list(map(int,input().split())) for _ in range(m)]

    def _most_neer(x,y, checkpoint):
        dist = float('inf')
        ans = 0
        for index, xy in enumerate(checkpoint):
            x2 = xy[0]
            y2 = xy[1]
            if dist > abs(x-x2) + abs(y-y2):
                dist = abs(x-x2) + abs(y-y2)
                ans = index + 1
        return ans

    for a,b in ab:
        print(_most_neer(a,b, cd))

