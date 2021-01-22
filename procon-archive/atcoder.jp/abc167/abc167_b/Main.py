import math
from decimal import *

if __name__ == "__main__":
    a,b,c,k = map(int,input().split())
    rest = 0
    if a >= k :
        print(k)
        exit()
    else:
        rest = k - a
        if b >= rest:
            print(a)
        else:
            rest = k - a -b
            if c >= rest:
                print(a-rest)
            else:
                print(a-c)


