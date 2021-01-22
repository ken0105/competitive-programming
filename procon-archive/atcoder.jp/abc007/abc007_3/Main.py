from collections import deque
if __name__ == '__main__':
    R,C = map(int,input().split())
    sy,sx = map(int,input().split())
    sy -= 1
    sx -= 1
    gy,gx = map(int,input().split())
    gy -= 1
    gx -= 1

    G = [[0] * C for _ in range(R)]
    for i in range(R):
        ss = input()
        for s in range(len(ss)):
            if ss[s] == ".":
                G[i][s] = 1

    def bfs(y,x):
        q = deque()
        q.append((y,x))
        d = [[-1] * C for _ in range(R)]
        d[y][x] = 0
        while q:
            now = q.popleft()
            now_y = now[0]
            now_x = now[1]
            top = G[now_y - 1][now_x]
            left = G[now_y][now_x -1]
            right = G[now_y][now_x + 1]
            bottom = G[now_y + 1][now_x]
            if top == 1 and d[now_y -1][now_x] == -1:
                q.append((now_y-1, now_x))
                d[now_y-1][now_x] = d[now_y][now_x] + 1
            if left == 1 and d[now_y][now_x -1] == -1:
                q.append((now_y, now_x-1))
                d[now_y][now_x-1] = d[now_y][now_x] + 1
            if right == 1 and d[now_y][now_x + 1] == -1:
                q.append((now_y, now_x +1))
                d[now_y][now_x + 1] = d[now_y][now_x] + 1
            if bottom == 1 and d[now_y+1][now_x] == -1:
                q.append((now_y+1, now_x))
                d[now_y+1][now_x] = d[now_y][now_x] + 1
        print(d[gy][gx])
    bfs(sy,sx)
