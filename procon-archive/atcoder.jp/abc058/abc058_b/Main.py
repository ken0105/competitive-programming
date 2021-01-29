from collections import deque

if __name__ == '__main__':
    o = deque(input())
    e = deque(input())

    ans = ""
    while len(o) > 0 or len(e) > 0:
        if len(o) > 0:
           ans += o.popleft()
        if len(e) > 0:
            ans += e.popleft()
    print(ans)