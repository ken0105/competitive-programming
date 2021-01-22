import math

if __name__ == "__main__":
    x, y, a, b = map(int, input().split())
    exp = 0
    flg = 0
    while x < y:
        mul = x * a
        pl = x + b
        if mul < pl:
            x = mul
            exp += 1
        else:
            x = pl
            exp += 1
            break
    if x >= y:
        exp -= 1
        print(exp)
        exit()
    exp = exp + (y-x-1)//b
    print(exp)
