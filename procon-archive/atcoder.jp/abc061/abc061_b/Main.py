if __name__ == '__main__':
    n,m = map(int,input().split())
    road = [0] * n
    for i in range(m):
        a,b = map(int,input().split())
        road[a-1] += 1
        road[b-1] += 1
    for r in road:
        print(r)