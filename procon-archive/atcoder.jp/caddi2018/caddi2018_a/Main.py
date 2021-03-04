import math


def main():
    n, p = map(int, input().split())
    d = {}
    if n == 1:
        print(p)
        exit()
    for i in range(2, int(math.sqrt(p)) + 1):
        while True:
            if p % i == 0:
                if d.get(i) is None:
                    d[i] = 1
                else:
                    d[i] += 1
                p //= i
            else:
                break
    ans = 1
    for i in list(d.keys()):
        while d[i] >= n:
            d[i] -= n
            ans *= i
    print(ans)



if __name__ == '__main__':
    main()
