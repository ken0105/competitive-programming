from collections import deque


def accompany(time, k, t):
    if not t or t[0] > time + k:
        return 1
    if t[0] <= time + k:
        t.popleft()
    return


def main():
    n,c,k = map(int,input().split())
    t = [int(input()) for _ in range(n)]
    t.sort()
    t = deque(t)
    ans = 0
    while t:
        ans += 1
        time = t.popleft()
        for _ in range(c - 1):
            r = accompany(time, k, t)
            if r == 1:
                break
    print(ans)


if __name__ == '__main__':
    main()