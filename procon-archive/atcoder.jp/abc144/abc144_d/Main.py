import math

if __name__ == "__main__":
    a, b, x = map(int, input().split())
    if a ** 2 * b / 2 < x:
        v = 2*x / a/a -b
        v = b - v
        t = math.degrees(math.atan(v / a))
        print(t)
    else:
        d = 2*x/b/a
        t = math.degrees(math.atan(d / b))
        print(90 - t)
