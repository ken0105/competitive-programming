import math


def main():
    n, m = map(int, input().split())
    s = input()
    t = input()
    lcm = n * m // math.gcd(n,m)
    t_n = lcm // n
    t_m = lcm // m
    gcd = t_n * t_m // math.gcd(t_n, t_m)
    if lcm == n * m and s[0] != t[0]:
        print(-1)
        exit()
    for i in range(lcm // gcd - 1):
        num = gcd * (i + 1)
        if s[num // t_n] != t[num // t_m]:
            print(-1)
            exit()
    print(lcm)



if __name__ == '__main__':
    main()