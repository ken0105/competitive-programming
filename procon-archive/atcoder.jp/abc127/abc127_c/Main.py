import re

if __name__ == '__main__':
    n,m = map(int,input().split())
    s = 1
    e = n
    for _ in range(m):
        l,r = map(int,input().split())
        s = max(s,l)
        e = min(e,r)
    ans = set(range(s,e+1))
    print(len(ans))