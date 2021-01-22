import math
from decimal import *

if __name__ == "__main__":
    s  = input()
    t = input()
    if s == t[:-1]:
        print("Yes")
    else:
        print("No")