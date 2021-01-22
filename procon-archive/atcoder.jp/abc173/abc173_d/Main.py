from collections import deque
if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ref = deque()
    ref.append(a.pop())
    ans = 0
    while a:
        try:
            r = a.pop()
            ref.append(r)
            ref.append(r)
            ans += ref.popleft()
        except:
            pass
    print(ans)