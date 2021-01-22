import math
from decimal import *
import numpy as np

if __name__ == '__main__':
    x,y,z = map(int,input().split())
    x,y = y,x
    x,z = z,x
    print(x,y,z)


