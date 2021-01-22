import math
from decimal import *

if __name__ == "__main__":
    k = int(input())
    s = input()

    if k < len(s):
        print(s[:k] + "...")
    else:
        print(s)
