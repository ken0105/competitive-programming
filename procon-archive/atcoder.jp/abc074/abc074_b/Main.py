import math

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    xs = list(map(int,input().split()))
    ans = 0
    for x in xs:
        ans += min(x, k -x) * 2
    print(ans)