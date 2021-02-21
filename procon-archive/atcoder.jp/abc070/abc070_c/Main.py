import math


def main():
    n = int(input())
    lcm = int(input())
    for _ in range(n-1):
        tmp = int(input())
        lcm = tmp * lcm // math.gcd(lcm, tmp)
    print(lcm)

if __name__ == '__main__':
    main()