import math

if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    total_gcd = 1

    def lcm(x, y):
        return x * y // math.gcd(x, y)
    for i, num in enumerate(a):
        total_gcd = lcm(total_gcd, num)

    ans = 0
    for num in a:
        ans += (total_gcd - 1) % num
    print(ans)


