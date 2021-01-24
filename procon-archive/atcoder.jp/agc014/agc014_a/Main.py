import math

if __name__ == '__main__':
    a,b,c = map(int,input().split())
    ans = 0
    seen = set()
    while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        if (a,b,c) in seen:
            print(-1)
            exit()
        seen.add((a,b,c))
        ans += 1
        a2,b2,c2 = a,b,c
        a = (b2+c2) /2
        b = (a2+c2) / 2
        c = (a2+b2) / 2
    print(ans)