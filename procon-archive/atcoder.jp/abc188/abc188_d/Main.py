from collections import defaultdict

if __name__ == "__main__":
    N,C = map(int,input().split())
    d = defaultdict(int)
    for i in range(N):
        a,b,c = map(int,input().split())
        d[a] += c
        d[b+1] -= c
    l = []
    for k,v in d.items():
        l.append([k,v])
    l.sort()
    services = 0
    ans = 0
    for i in range(len(l)):
        if i + 1 == len(l):
            break
        duration = l[i+1][0] - l[i][0]
        services += l[i][1]
        act_charge = min(services,C)
        ans += act_charge * duration
    print(ans)