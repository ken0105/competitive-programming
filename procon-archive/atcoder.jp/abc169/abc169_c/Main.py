import math
from decimal import *

if __name__ == "__main__":
    x,y = map(Decimal, input().split())

    ans = math.floor(x * y )
    print(ans)