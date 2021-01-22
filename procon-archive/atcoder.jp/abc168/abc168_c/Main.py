import math
from decimal import *

if __name__ == "__main__":
    a, b, h, m = map(int, input().split())

    h_angle = 30 * h + m * 0.5
    m_angle = 6 * m
    dif = h_angle - m_angle
    if dif > 180:
        dif = 360 - dif

    rad = math.cos(math.radians(dif))
    ans = (a ** 2 + b ** 2 - 2 * a * b * rad) ** 0.5
    print(ans)