import cmath


def main():
    n = int(input())
    x,y = map(int, input().split())
    x2,y2 = map(int, input().split())
    p0 = complex(x,y)
    pn2 = complex(x2,y2)
    o = (p0 + pn2) / 2
    r = cmath.rect(1, cmath.pi * 2 / n)
    ans = (p0 - o) * r + o
    print(ans.real, ans.imag)

if __name__ == '__main__':
    main()
