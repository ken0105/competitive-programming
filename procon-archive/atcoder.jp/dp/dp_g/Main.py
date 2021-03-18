import sys
sys.setrecursionlimit(10000000)
length, done, g = [], [], []

def main():
    n,m = map(int, input().split())
    global g
    g = [[] for _ in range(n)]
    indeg = [0 for _ in range(n)]
    for _ in range(m):
        x,y = map(int, input().split())
        g[x-1].append(y-1)
        indeg[y-1] += 1

    global length, done
    length = [0 for _ in range(n)]
    done = [False for _ in range(n)]

    ans = 0
    for i in range(n):
        if indeg[i] == 0:
            ans = max(ans, rec(i))
    print(ans)

def rec(i):
    if done[i]:
        return length[i]
    max_length = 0
    for j in g[i]:
        max_length = max(max_length, rec(j) + 1)
    done[i] = True
    length[i] = max_length
    return max_length

if __name__ == '__main__':
    main()