import math
from collections import deque

if __name__ == '__main__':
    l = list(map(int,input().split()))
    l.sort()
    a = l[0]
    b = l[1]
    c = l[2]

    x = math.floor(c/2)
    y = math.ceil(c/2)
    print(abs(b*a*x - b*a*y))



