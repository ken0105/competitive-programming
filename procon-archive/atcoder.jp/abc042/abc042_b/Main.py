from collections import deque

if __name__ == '__main__':
    n,l = map(int,input().split())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    ans = ""
    for i in s:
        ans += i
    print(ans)




