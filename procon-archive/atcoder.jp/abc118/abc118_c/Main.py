import math


def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = math.gcd(a[0],a[1])
    for i in range(2,n):
        ans = math.gcd(ans, a[i])
    print(ans)

if __name__ == '__main__':
    main()