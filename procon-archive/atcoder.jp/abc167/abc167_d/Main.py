if __name__ == '__main__':
    N,K = map(int,input().split())
    A = [0] + list(map(int,input().split()))
    seen = set()
    seen.add(1)
    visited = [1]
    now = 1
    cnt = 0
    while len(seen) == len(visited):
        now = A[now]
        seen.add(now)
        visited.append(now)
        cnt += 1
        if cnt == K:
            break

    first = visited.index(now)
    second = len(visited) - 1
    loop_size = second - first
    if loop_size != 0:
        r = (K - first) % loop_size
    else:
        r = 0
    ans = visited[first + r]
    print(ans)

