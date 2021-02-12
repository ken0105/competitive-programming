from math import gcd


def main():
    N,X = map(int,input().split())
    x = list(map(int,input().split()))
    ans = abs(x[0] - X)
    for num in x:
        ans = gcd(ans, abs(num - X))
    print(ans)



if __name__ == '__main__':
    main()